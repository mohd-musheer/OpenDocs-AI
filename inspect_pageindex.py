"""
scripts/inspect_pageindex.py

Run from the project root BEFORE restarting the server:
    python scripts/inspect_pageindex.py

This script tells you:
  1. How many .json files are in data/pageindex/
  2. The top-level keys of the first file
  3. The first root node's keys and a preview of its text/summary
  4. A simulated keyword search so you can see the fix working offline

Usage:
    python scripts/inspect_pageindex.py
    python scripts/inspect_pageindex.py --query "fastapi routes"
"""

import json
import sys
from pathlib import Path

PAGEINDEX_DIR = Path("data/raw")


def load_all_trees():
    trees = []
    if not PAGEINDEX_DIR.exists():
        print(f"ERROR: {PAGEINDEX_DIR} does not exist.")
        return trees
    files = list(PAGEINDEX_DIR.glob("*.json"))
    print(f"Found {len(files)} file(s) in {PAGEINDEX_DIR}/\n")
    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            trees.append((f.name, json.load(fh)))
    return trees


def inspect_tree(name, tree):
    print(f"=== {name} ===")
    print(f"Top-level keys: {list(tree.keys())}")
    print(f"doc_name       : {tree.get('doc_name', '(missing)')}")
    print(f"doc_description: {str(tree.get('doc_description', '(missing)'))[:120]}")
    print(f"line_count     : {tree.get('line_count', '(missing)')}")

    structure = tree.get("structure", [])
    print(f"structure nodes (root level): {len(structure)}")

    if structure:
        first = structure[0]
        print(f"\nFirst root node keys: {list(first.keys())}")
        print(f"  title         : {first.get('title', '(missing)')}")
        print(f"  node_id       : {first.get('node_id', '(missing)')}")
        print(f"  line_num      : {first.get('line_num', '(missing)')}")
        text_preview = (first.get("text") or first.get("summary") or "")[:200]
        print(f"  text/summary  : {text_preview!r}")
        child_nodes = first.get("nodes", [])
        print(f"  child nodes   : {len(child_nodes)}")
    print()


def _collect_all_text(node, parts):
    if not isinstance(node, dict):
        return
    for field in ("title", "summary", "prefix_summary", "text"):
        val = node.get(field)
        if val and isinstance(val, str):
            parts.append(val)
    for child in node.get("nodes", []):
        _collect_all_text(child, parts)


def simulate_retrieve(trees, query: str, top_k: int = 3):
    query_words = set(query.lower().split())
    results = []
    for name, tree in trees:
        parts = []
        for field in ("doc_name", "doc_description"):
            val = tree.get(field)
            if val:
                parts.append(val)
        for root_node in tree.get("structure", []):
            _collect_all_text(root_node, parts)
        full_text = "\n".join(parts).lower()

        score = sum(1 for w in query_words if len(w) >= 3 and w in full_text)
        if score > 0:
            results.append((score, name))

    results.sort(reverse=True)

    print(f"\n--- Simulated retrieve('{query}') ---")
    if results:
        for score, name in results[:top_k]:
            print(f"  score={score}  file={name}")
    else:
        print("  No results — check that build_pageindex.py ran successfully")
        print("  and that data/markdown/ contains .md files with ## headings.")
    print()


def main():
    query = "what is fastapi"
    if len(sys.argv) > 1 and sys.argv[1] == "--query" and len(sys.argv) > 2:
        query = " ".join(sys.argv[2:])

    trees = load_all_trees()
    if not trees:
        return

    # Inspect first 3 files
    for name, tree in trees[:3]:
        inspect_tree(name, tree)

    # Simulate retrieval
    simulate_retrieve(trees, query)
    simulate_retrieve(trees, "routes path parameters")


if __name__ == "__main__":
    main()