"""
app/agent/agent.py

Changes vs original:
  - context assembly now reads the new doc format:
      { doc_name, doc_description, matched_nodes: [{title, text, summary, ...}] }
    instead of blindly calling doc.get("doc_description", str(doc)).
  - Each matched node's title + text/summary is included in the LLM prompt
    so the model actually has documentation content to answer from.
"""

import re

from app.pageindex_engine.retrieve import retrieve

from app.llm.groq_client import ask_llm

from app.memory.session_memory import (
    save_memory,
    get_memory,
)

from app.memory.profile_memory import get_profile
from app.memory.summary_memory import get_summary
from app.memory.chat_memory import get_recent
from app.memory.memory_manager import save_conversation


def _format_docs(docs: list) -> str:
    """
    Convert the list of retrieved doc dicts into a plain-text block
    that can be dropped into the LLM prompt.
    """
    if not docs:
        return ""

    sections: list[str] = []

    for idx, doc in enumerate(docs, 1):
        if not isinstance(doc, dict):
            sections.append(str(doc))
            continue

        header_parts = []
        if doc.get("doc_name"):
            header_parts.append(f"Document: {doc['doc_name']}")
        if doc.get("doc_description"):
            header_parts.append(f"Description: {doc['doc_description']}")

        section_lines = [f"--- Source {idx} ---"]
        if header_parts:
            section_lines.extend(header_parts)

        for node in doc.get("matched_nodes", []):
            if not isinstance(node, dict):
                continue
            title = node.get("title", "")
            # Prefer the full text; fall back to summary / prefix_summary
            content = (
                node.get("text")
                or node.get("summary")
                or node.get("prefix_summary")
                or ""
            )
            if title:
                section_lines.append(f"\n## {title}")
            if content:
                # Trim extremely long nodes to avoid blowing up the prompt
                section_lines.append(content[:3000])

        sections.append("\n".join(section_lines))

    return "\n\n".join(sections)


def ask_docs(question: str) -> str:

    # =========================================================
    # Save simple facts from user message
    # =========================================================
    name_match = re.search(
        r"my name is ([a-zA-Z ]+?)(?: and |,|\.|$)",
        question,
        re.IGNORECASE,
    )
    if name_match:
        name = name_match.group(1).strip()
        save_memory("name", name)
        question = question.replace(name_match.group(0), "").strip()

    # =========================================================
    # Load memory
    # =========================================================
    session_memory = get_memory()
    profile        = get_profile()
    summary        = get_summary()
    recent         = get_recent()

    # =========================================================
    # Retrieve docs
    # =========================================================
    docs, confidence = retrieve(question)

    print("\n" + "=" * 80)
    print("RETRIEVAL CONFIDENCE")
    print("=" * 80)
    print(confidence)
    print(len(docs))

    context = _format_docs(docs)

    print("\n" + "=" * 80)
    print("RETRIEVED DOCS")
    print("=" * 80)
    if docs:
        for idx, doc in enumerate(docs):
            print(f"\nDOC {idx + 1}: {doc.get('doc_name', '?')}")
            desc = doc.get("doc_description", "")
            if desc:
                print(f"  Description: {desc[:200]}")
            for node in doc.get("matched_nodes", []):
                print(f"  Node: {node.get('title', '?')}")
    else:
        print("(none)")

    # =========================================================
    # Build prompt
    # =========================================================
    prompt = f"""You are OpenDocs AI.

Session Memory:
{session_memory}

User Profile:
{profile}

Conversation Summary:
{summary}

Recent Conversation:
{recent}

Documentation Context:
{context}

Question:
{question}

Instructions:
1. Use the documentation context above to answer the question.
2. Use memory if the user asks personal questions.
3. If the answer is not in the docs, clearly say it is not available.
4. Do not invent documentation.

Answer:"""

    print("\n" + "=" * 80)
    print("FINAL PROMPT")
    print("=" * 80)
    print(prompt)

    # =========================================================
    # LLM call
    # =========================================================
    answer = ask_llm(prompt)

    print("\n" + "=" * 80)
    print("LLM ANSWER")
    print("=" * 80)
    print(answer)

    # =========================================================
    # Save conversation
    # =========================================================
    save_conversation(question, answer)

    return answer