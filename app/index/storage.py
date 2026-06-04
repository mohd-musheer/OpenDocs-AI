import json
from pathlib import Path

TREE_PATH = Path(
    "data/processed/tree.json"
)


def save_tree(tree):

    TREE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        TREE_PATH,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            tree,
            f,
            ensure_ascii=False,
            indent=2
        )


def load_tree():

    if not TREE_PATH.exists():
        return []

    with open(
        TREE_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)