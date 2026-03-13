# Degree Jobs Fresher Bot

Telegram bot that scrapes and posts fresher job opportunities in Hyderabad.

## Features

- **Scrapes from:** LinkedIn public API
- **Target:** Any degree fresher jobs (0-1 years experience)
- **Location:** Hyderabad only
- **Update frequency:** Every 5 minutes
- **Posting:** Posts to Telegram with job details

## Setup

1. Create a Telegram bot via @BotFather
2. Get your chat ID (the channel where jobs will be posted)
3. Set environment variables:
   - `BOT_TOKEN`: Your Telegram bot token
   - `CHAT_ID`: Target channel/chat ID

## Running

```bash
python bot.py
```

Single-cycle execution (designed for GitHub Actions cron jobs).

## Files

- `bot.py` - Main bot logic (single-cycle)
- `scraper.py` - LinkedIn job scraping
- `sender.py` - Telegram posting
- `config.py` - Configuration
- `requirements.txt` - Dependencies
