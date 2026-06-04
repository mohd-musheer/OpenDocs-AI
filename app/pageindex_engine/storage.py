import json
from pathlib import Path

PAGEINDEX_DIR = Path(
    "data/pageindex"
)


def save_tree(
    name,
    tree
):

    PAGEINDEX_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    path = (
        PAGEINDEX_DIR /
        f"{name}.json"
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            tree,
            f,
            ensure_ascii=False,
            indent=2
        )


def load_all_trees():

    trees = []

    if not PAGEINDEX_DIR.exists():
        return trees

    for file in PAGEINDEX_DIR.glob(
        "*.json"
    ):

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            trees.append(
                json.load(f)
            )

    return trees