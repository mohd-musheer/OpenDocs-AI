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

    print("\nLOADING PAGEINDEX FILES")
    print("DIRECTORY:", PAGEINDEX_DIR.absolute())

    if not PAGEINDEX_DIR.exists():
        print("DIRECTORY DOES NOT EXIST")
        return trees

    files = list(PAGEINDEX_DIR.glob("*.json"))

    print("FILES FOUND:", len(files))

    for file in files:

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                trees.append(
                    json.load(f)
                )

        except Exception as e:

            print(
                f"ERROR LOADING {file}: {e}"
            )

    print(
        "TREES LOADED:",
        len(trees)
    )

    return trees