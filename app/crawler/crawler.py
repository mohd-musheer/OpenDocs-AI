import json
from pathlib import Path

from sitemap import get_urls_from_sitemap
from extractor import extract_page


DATA_DIR = Path("data/raw")


def save_document(doc: dict):

    DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    filename = (
        doc["url"]
        .replace("https://", "")
        .replace("/", "_")
    )

    filepath = DATA_DIR / f"{filename}.json"

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            doc,
            f,
            ensure_ascii=False,
            indent=2
        )


def crawl_site(
    sitemap_url: str,
    limit: int | None = None
):

    urls = get_urls_from_sitemap(
        sitemap_url
    )

    if limit:
        urls = urls[:limit]

    print(
        f"Found {len(urls)} URLs"
    )

    success = 0

    for url in urls:

        try:

            document = extract_page(url)

            if not document:
                continue

            save_document(document)

            success += 1

            print(
                f"[{success}] {url}"
            )

        except Exception as e:

            print(
                f"ERROR: {url}"
            )

            print(e)

    print(
        f"\nFinished: {success} pages"
    )


if __name__ == "__main__":

    data = crawl_site(
        sitemap_url=
        "https://fastapi.tiangolo.com/sitemap.xml"
    )
    print(data)
    