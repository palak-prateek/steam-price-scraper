import logging
import time

from config import CHECK_INTERVAL, GAME_NAME, STEAM_URL, TARGET_PRICE
from notifier import send_email
from scraper import get_price

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def check_price() -> None:
    logger.info("Checking Steam price for %s...", GAME_NAME)

    price = get_price(STEAM_URL)

    if price is None:
        return

    logger.info("Current price: ₹%.2f", price)

    if price <= TARGET_PRICE:
        logger.info("Target price reached! Sending email notification...")
        send_email(price)
    else:
        logger.info("Price is above target (₹%.2f).", TARGET_PRICE)


if __name__ == "__main__":
    logger.info("Steam Price Scraper started.")

    while True:
        check_price()
        logger.info("Sleeping for %d seconds.", CHECK_INTERVAL)
        time.sleep(CHECK_INTERVAL)