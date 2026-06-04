import trafilatura
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def clean_text(text: str) -> str:
    """
    Basic cleanup
    """

    if not text:
        return ""

    text = text.replace("\xa0", " ")
    text = text.replace("\n\n\n", "\n\n")

    return text.strip()


def extract_title(html: str) -> str:

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    if soup.title:
        return soup.title.text.strip()

    return ""




import requests
import trafilatura
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def extract_page(url):

    response = requests.get(
        url,
        timeout=30
    )

    html = response.text

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    title = ""

    if soup.title:
        title = soup.title.text.strip()

    downloaded = trafilatura.extract(
        html
    )

    return {
        "url": url,
        "title": title,
        "domain": urlparse(url).netloc,
        "content": downloaded
    }