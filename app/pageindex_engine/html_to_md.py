import json
from pathlib import Path

RAW_DIR = Path("data/raw")
MD_DIR = Path("data/markdown")


def convert_all():

    MD_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    files = list(
        RAW_DIR.glob("*.json")
    )

    print(
        f"Found {len(files)} raw files"
    )

    for file in files:

        print(
            f"Converting: {file.name}"
        )

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        md_content = f"""
# {data.get('title', '')}

URL: {data.get('url', '')}

{data.get('content', '')}
"""

        out_file = (
            MD_DIR /
            f"{file.stem}.md"
        )

        with open(
            out_file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(md_content)

    print(
        f"Created {len(files)} markdown files"
    )


if __name__ == "__main__":

    convert_all()