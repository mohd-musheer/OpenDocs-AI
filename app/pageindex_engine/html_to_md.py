import json
from pathlib import Path

RAW_DIR = Path("data/raw")
MD_DIR = Path("data/markdown")


def convert_all():

    MD_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    for file in RAW_DIR.glob("*.json"):

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        md_content = f"""
# {data['title']}

URL: {data['url']}

{data['content']}
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

    print("Markdown created")