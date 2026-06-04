import asyncio
import json
from pathlib import Path

from pageindex.page_index_md import (
    md_to_tree
)

from app.pageindex_engine.storage import (
    save_tree
)

MD_DIR = Path(
    "data/markdown"
)


async def build():

    for md_file in MD_DIR.glob(
        "*.md"
    ):

        result = await md_to_tree(
            md_path=str(md_file),

            if_thinning=False,

            if_add_node_summary="no",

            if_add_doc_description="no",

            if_add_node_text="yes",

            if_add_node_id="yes"
        )

        save_tree(
            md_file.stem,
            result
        )

        print(
            f"Indexed {md_file.name}"
        )


if __name__ == "__main__":
    asyncio.run(build())