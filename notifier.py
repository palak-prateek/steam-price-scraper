import logging

import resend

from config import EMAIL_FROM, EMAIL_TO, RESEND_API_KEY, GAME_NAME, STEAM_URL

logger = logging.getLogger(__name__)

resend.api_key = RESEND_API_KEY


def send_email(price: float) -> None:
    subject = f"🎮 {GAME_NAME} Price Alert 🔔"

    html = f"""
    <h2>📉 Price Drop Detected 📉</h2>

    <h2>{GAME_NAME} is now available for ₹{price:.2f}.</h2>

    <p>
        <a href="{STEAM_URL}">View on Steam</a>
    </p>

    <hr>

    <p>Sent automatically by Steam Price Scraper.</p>
    """

    resend.Emails.send(
        {
            "from": EMAIL_FROM,
            "to": EMAIL_TO,
            "subject": subject,
            "html": html,
        }
    )

    logger.info("Price alert email sent successfully.")
