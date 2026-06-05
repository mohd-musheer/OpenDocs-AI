import json
import re
from pathlib import Path

from app.crawler.sitemap import get_urls
from app.crawler.extractor import extract_page

RAW_DIR = Path("data/raw")

def sanitize_filename(url: str) -> str:


    filename = (
        url.replace("https://", "")
        .replace("http://", "")
        .replace("/", "_")
        .replace("?", "_")
        .replace("&", "_")
        .replace("=", "_")
        .replace(":", "_")
    )

    filename = re.sub(
        r'[<>:"/\\|?*]',
        "_",
        filename
    )

    return filename[:200]

def save_page(page: dict, url: str):


    filename = sanitize_filename(url)

    out_file = (
        RAW_DIR /
        f"{filename}.json"
    )

    counter = 1

    while out_file.exists():

        out_file = (
            RAW_DIR /
            f"{filename}_{counter}.json"
        )

        counter += 1

    with open(
        out_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            page,
            f,
            ensure_ascii=False,
            indent=2
        )


def crawl_site(source):

    RAW_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    max_pages = source.get(
        "max_pages",
        100
    )

    urls = get_urls(source)

    urls = list(
        dict.fromkeys(urls)
    )

    urls = urls[:max_pages]

    print(
        f"\nPROCESSING {len(urls)} URLS"
    )

    success = 0
    failed = 0
    skipped = 0

    for i, url in enumerate(
        urls,
        start=1
    ):

        try:

            print(
                f"[{i}/{len(urls)}] {url}"
            )

            page = extract_page(url)

            if not page:

                skipped += 1
                continue

            content = page.get(
                "content",
                ""
            )

            if not content:

                skipped += 1

                print(
                    "SKIPPED EMPTY PAGE"
                )

                continue

            save_page(
                page,
                url
            )

            success += 1

        except Exception as e:

            failed += 1

            print(
                f"FAILED: {url}"
            )

            print(
                f"ERROR: {str(e)}"
            )

    print(
        "\n" + "=" * 80
    )

    print(
        f"DONE: {source['name']}"
    )

    print(
        f"SUCCESS : {success}"
    )

    print(
        f"SKIPPED : {skipped}"
    )

    print(
        f"FAILED  : {failed}"
    )

    print(
        "=" * 80
    )


def crawl_all():

    possible_paths = [

        Path("/app/sources.json"),

        Path("sources.json"),

        Path("app/sources.json"),
    ]

    sources_file = None

    for p in possible_paths:

        if p.exists() and p.is_file():

            sources_file = p

            break

    if sources_file is None:

        raise FileNotFoundError(
            "sources.json not found"
        )

    print(
        f"\nUSING SOURCES FILE: {sources_file.absolute()}"
    )

    with open(
        sources_file,
        "r",
        encoding="utf-8"
    ) as f:

        sources = json.load(f)

    print(
        f"\nTOTAL SOURCES: {len(sources)}"
    )

    for source in sources:

        print(
            "\n" + "=" * 80
        )

        print(
            f"CRAWLING: {source['name']}"
        )

        print(
            f"URL: {source['url']}"
        )

        print(
            "=" * 80
        )

        try:

            crawl_site(
                source
            )

        except Exception as e:

            print(
                f"\nFAILED SOURCE: {source['name']}"
            )

            print(e)

    print(
        "\nALL SOURCES FINISHED"
    )
