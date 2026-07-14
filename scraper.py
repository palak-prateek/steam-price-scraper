import logging

import requests
from bs4 import BeautifulSoup

from typing import Optional

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

session = requests.Session()
session.headers.update(HEADERS)


def get_price(url: str) -> Optional[float]:
    """
    Scrape the current Steam price.

    Returns:
        float: Current game price.
        None: If the price cannot be retrieved.
    """

    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Find the first element containing Steam's price data.
        price_element = soup.find(attrs={"data-price-final": True})

        if not price_element:
            logger.error("Price element not found.")
            return None

        # Steam stores prices in the smallest currency unit
        # (e.g. paise for INR), so divide by 100.
        price = int(price_element["data-price-final"]) / 100

        return price

    except requests.RequestException as e:
        logger.error("Request failed: %s", e)

    except Exception:
        logger.exception("Unexpected error while scraping Steam.")

    return None
