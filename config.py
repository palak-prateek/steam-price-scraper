import os
from dotenv import load_dotenv

load_dotenv()

GAME_NAME = os.getenv("GAME_NAME")

STEAM_URL = os.getenv("STEAM_URL")

TARGET_PRICE = float(os.getenv("TARGET_PRICE", "0"))

CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "86400"))

RESEND_API_KEY = os.getenv("RESEND_API_KEY")

EMAIL_FROM = os.getenv("EMAIL_FROM")

EMAIL_TO = os.getenv("EMAIL_TO")
