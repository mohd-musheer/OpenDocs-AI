import requests
from bs4 import BeautifulSoup


def get_urls_from_sitemap(sitemap_url: str) -> list[str]:
    """
    Extract all URLs from sitemap.xml
    """

    response = requests.get(
        sitemap_url,
        timeout=30
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "xml"
    )

    urls = []

    for loc in soup.find_all("loc"):
        urls.append(loc.text.strip())

    return urls