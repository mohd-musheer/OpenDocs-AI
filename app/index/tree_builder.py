import json
from pathlib import Path

from app.index.storage import save_tree

RAW_DIR = Path(
    "data/raw"
)


def build_index():

    documents = []

    files = list(
        RAW_DIR.glob("*.json")
    )

    for file in files:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            doc = json.load(f)

        documents.append(
            {
                "node_id": file.stem,
                "title": doc.get(
                    "title",
                    file.stem
                ),
                "url": doc.get(
                    "url"
                ),
                "content": doc.get(
                    "content",
                    ""
                )
            }
        )

    save_tree(documents)

    print(
        f"Indexed {len(documents)} documents"
    )


if __name__ == "__main__":
    build_index()