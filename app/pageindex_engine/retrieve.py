"""
app/pageindex_engine/retrieve.py

Root-cause fix:
  The old extract_text() walked tree["structure"] but looked for
  node.get("children", []) to descend.  PageIndex NEVER uses the key
  "children" — every node stores its child nodes under "nodes".
  That single wrong key name caused the traversal to visit only the
  top-level node of each tree and then stop, so virtually no text was
  searched and the score was always 0.

  Additionally the old code skipped the node 'title' field entirely,
  which is the most reliable keyword signal for doc-retrieval.

  This version:
    1.  Walks every node recursively using the correct key "nodes".
    2.  Indexes title + summary + prefix_summary + text for each node.
    3.  Also indexes the top-level doc_name and doc_description.
    4.  Returns the matched doc objects with the best-match nodes
        included so that agent.py can forward the real text to the LLM.
"""

from app.pageindex_engine.storage import load_all_trees


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _collect_all_text(node, parts: list[str]) -> None:
    """
    Recursively walk a PageIndex node (dict) and collect every searchable
    text field into `parts`.

    PageIndex MD-tree nodes contain:
        title, node_id, line_num, summary, prefix_summary, text, nodes
    """
    if not isinstance(node, dict):
        return

    for field in ("title", "summary", "prefix_summary", "text"):
        value = node.get(field)
        if value and isinstance(value, str):
            parts.append(value)

    for child in node.get("nodes", []):
        _collect_all_text(child, parts)


def _tree_to_searchable_text(tree: dict) -> str:
    """
    Convert a full PageIndex document tree (as saved by save_tree) into a
    single lowercase string for keyword matching.

    A saved tree has the shape:
        {
            "doc_name": "...",
            "doc_description": "...",   # optional
            "line_count": N,
            "structure": [ <node>, <node>, ... ]
        }
    """
    parts: list[str] = []

    # Top-level metadata
    for field in ("doc_name", "doc_description"):
        value = tree.get(field)
        if value and isinstance(value, str):
            parts.append(value)

    # Walk the structure (list of root nodes)
    for root_node in tree.get("structure", []):
        _collect_all_text(root_node, parts)

    return "\n".join(parts).lower()


def _best_nodes_for_question(tree: dict, query_words: set[str], top_k_nodes: int = 3) -> list[dict]:
    """
    Walk every node in the tree and return the top_k_nodes whose text /
    summary fields best match the query keywords.  This gives the LLM the
    most relevant excerpts rather than the full (potentially huge) tree.
    """
    candidates: list[tuple[int, dict]] = []

    def _score_node(node: dict) -> None:
        if not isinstance(node, dict):
            return
        node_parts: list[str] = []
        for field in ("title", "summary", "prefix_summary", "text"):
            value = node.get(field)
            if value and isinstance(value, str):
                node_parts.append(value)
        node_text = " ".join(node_parts).lower()
        score = sum(1 for w in query_words if len(w) >= 3 and w in node_text)
        if score > 0:
            candidates.append((score, node))
        for child in node.get("nodes", []):
            _score_node(child)

    for root_node in tree.get("structure", []):
        _score_node(root_node)

    candidates.sort(key=lambda x: x[0], reverse=True)
    return [node for _, node in candidates[:top_k_nodes]]


# ---------------------------------------------------------------------------
# Public interface — called by agent.py
# ---------------------------------------------------------------------------

def retrieve(question: str, top_k: int = 5):
    """
    Return (docs, confidence) where:
        docs       — list of dicts, each containing:
                       doc_name, doc_description, matched_nodes
        confidence — keyword hit count of the top result (0 if none)
    """
    trees = load_all_trees()

    print(f"\nTOTAL TREES LOADED: {len(trees)}")

    query_words = set(question.lower().split())

    results: list[tuple[int, dict]] = []

    for tree in trees:
        full_text = _tree_to_searchable_text(tree)

        score = sum(
            1 for word in query_words
            if len(word) >= 3 and word in full_text
        )

        if score > 0:
            results.append((score, tree))

    # Sort descending by score
    results.sort(key=lambda x: x[0], reverse=True)

    docs: list[dict] = []
    for score, tree in results[:top_k]:
        best_nodes = _best_nodes_for_question(tree, query_words, top_k_nodes=3)

        # Build a clean, LLM-friendly doc summary
        doc_entry = {
            "doc_name":        tree.get("doc_name", ""),
            "doc_description": tree.get("doc_description", ""),
            "matched_nodes":   best_nodes,
        }
        docs.append(doc_entry)

    confidence = results[0][0] if results else 0
    return docs, confidence