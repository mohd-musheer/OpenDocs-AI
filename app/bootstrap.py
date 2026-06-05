import asyncio
import shutil
from pathlib import Path

from app.crawler.crawler import crawl_all

from app.pageindex_engine.html_to_md import (
    convert_all
)

from app.pageindex_engine.build_pageindex import (
    build
)


async def bootstrap():

    raw_dir = Path("data/raw")
    md_dir = Path("data/markdown")
    pageindex_dir = Path("data/pageindex")

    print("\n" + "=" * 80)
    print("CLEARING OLD DATA")
    print("=" * 80)

    shutil.rmtree(raw_dir, ignore_errors=True)
    shutil.rmtree(md_dir, ignore_errors=True)
    shutil.rmtree(pageindex_dir, ignore_errors=True)

    raw_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    md_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    pageindex_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    print("STEP 1 - Crawling")
    crawl_all()

    print("STEP 2 - Markdown")
    convert_all()

    print("STEP 3 - PageIndex")
    await build()

    print("DONE")


if __name__ == "__main__":
    asyncio.run(
        bootstrap()
    )