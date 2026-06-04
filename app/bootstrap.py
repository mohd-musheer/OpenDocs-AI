import asyncio

from app.crawler.crawler import crawl_all

from app.pageindex_engine.html_to_md import (
    convert_all
)

from app.pageindex_engine.build_pageindex import (
    build
)


async def bootstrap():

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