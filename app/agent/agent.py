from app.index.tree_search import keyword_retrieve
from app.llm.groq_client import ask_llm


def ask_docs(question):

    docs = keyword_retrieve(
        question,
        top_k=5
    )

    context = ""

    for doc in docs:

        context += f"""
Title:
{doc['title']}

URL:
{doc['url']}

Content:
{doc['content'][:3000]}

------------------
"""

    prompt = f"""
Answer using only the documentation below.

{context}

Question:
{question}

Answer:
"""

    return ask_llm(prompt)