import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque


def get_urls_from_sitemap(sitemap_url):

    urls = []

    response = requests.get(
        sitemap_url,
        timeout=30
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "xml"
    )

    if soup.find("urlset"):

        for loc in soup.find_all("loc"):

            urls.append(
                loc.text.strip()
            )

        return urls

    if soup.find("sitemapindex"):

        for loc in soup.find_all("loc"):

            child = loc.text.strip()

            try:

                urls.extend(
                    get_urls_from_sitemap(
                        child
                    )
                )

            except Exception as e:

                print(
                    f"FAILED SUB SITEMAP: {child}"
                )

                print(e)

        return urls

    return urls


def crawl_links(
    start_url,
    max_pages=100
):

    visited = set()

    queue = deque(
        [start_url]
    )

    domain = urlparse(
        start_url
    ).netloc

    urls = []

    while queue and len(urls) < max_pages:

        url = queue.popleft()

        if url in visited:
            continue

        visited.add(url)

        try:

            response = requests.get(
                url,
                timeout=20
            )

            response.raise_for_status()

            urls.append(url)

            print(
                f"DISCOVERED {len(urls)}: {url}"
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            for link in soup.find_all(
                "a",
                href=True
            ):

                next_url = urljoin(
                    url,
                    link["href"]
                )

                parsed = urlparse(
                    next_url
                )

                if parsed.netloc != domain:
                    continue

                if "#" in next_url:
                    next_url = next_url.split(
                        "#"
                    )[0]

                if next_url not in visited:
                    queue.append(
                        next_url
                    )

        except Exception:
            pass

    return urls


def get_urls(
    source
):

    sitemap_url = source.get(
        "sitemap"
    )

    homepage = source["url"]

    max_pages = source.get(
        "max_pages",
        100
    )

    if sitemap_url:

        try:

            print(
                f"TRYING SITEMAP: {sitemap_url}"
            )

            urls = get_urls_from_sitemap(
                sitemap_url
            )

            if urls:

                print(
                    f"SITEMAP SUCCESS: {len(urls)} URLS"
                )

                return urls[:max_pages]

        except Exception as e:

            print(
                f"SITEMAP FAILED"
            )

            print(e)

    print(
        "USING LINK DISCOVERY"
    )

    return crawl_links(
        homepage,
        max_pages
    )