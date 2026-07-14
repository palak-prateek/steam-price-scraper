# Steam Price Scraper

A lightweight Python application that scrapes the Steam Store for a game's current price and sends an email notification when the price falls below a user-defined target.

This project demonstrates web scraping, environment-based configuration, automated email notifications, and scheduled execution using Python.

---

## Features

* 🎮 Scrapes the latest game price directly from the Steam Store.
* 📉 Detects when the current price falls below a target price.
* 📧 Sends automated email notifications using Resend.
* ⚙️ Stores configuration securely with environment variables.
* 📝 Logs application events and errors for easier debugging.
* ⏱️ Runs continuously with a configurable check interval.

---

## Tech Stack

* Python
* Requests
* BeautifulSoup4
* Resend

---

## Project Structure

```text
steam-price-scraper/
│
├── main.py          # Application entry point
├── scraper.py       # Steam price scraper
├── notifier.py      # Email notifications
├── config.py        # Environment configuration
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd steam-price-scraper
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.

```env
GAME_NAME=game_you_want_to_track

STEAM_URL=steam_url_for_the_game

TARGET_PRICE=your_preferred_price

CHECK_INTERVAL=86400

RESEND_API_KEY=your_resend_api_key

EMAIL_FROM=onboarding@resend.dev

EMAIL_TO=your_email
```

---

## Running the Project

Start the application:

```bash
python main.py
```

The scraper will periodically check the Steam Store and send an email whenever the game's price is less than or equal to the configured target price.

---

## Example Notification



---

## Future Improvements

* Support multiple Steam games.
* Store historical price data.
* Discord notifications.
* Docker support.
