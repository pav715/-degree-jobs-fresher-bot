# Degree Jobs Fresher — Hyderabad & Telangana Bot

Telegram bot that finds and posts fresher job opportunities in Hyderabad and Telangana for all degree types (B.Tech, M.Tech, B.Sc, M.Sc, BCA, MCA, B.Com, MBA, Fine Arts, Design, etc.).

## Features

✅ **Fresher-Only Jobs** - Filters for entry-level positions (0-1 years experience)
✅ **All Degree Types** - B.Tech, M.Tech, B.Sc, M.Sc, BCA, MCA, B.Com, MBA, Fine Arts, Design, etc.
✅ **Hyderabad & Telangana Only** - Location filtering ensures relevant jobs
✅ **Multi-Source Scraping** - LinkedIn, Google Jobs, Workday ATS, India Portals, Company Sites
✅ **No Duplicates** - Tracks seen jobs to prevent spam
✅ **Real-Time Updates** - Checks every 5 minutes
✅ **Newest First** - Most recent postings appear first

## Sources

- **LinkedIn Jobs** - Search filtered for freshers
- **Google Jobs** - Google job listings
- **Workday ATS** - Accenture, Wipro, TCS, Infosys, etc.
- **India Portals** - Naukri, Foundit, Shine, TimesJobs
- **Company Career Sites** - Direct career pages

## Setup

### 1. Clone/Download
```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create Telegram Channel
1. Create a channel named **"Degree Jobs Fresher-Hyd"**
2. Add this bot as **Admin** with **Post messages** permission
3. Send a test message to the channel

### 4. Set Environment Variables (Optional)
```bash
set BOT_TOKEN=8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0
```

Or update in `config.py` directly.

### 5. Run the Bot
```bash
python bot.py
```

On first run, the bot will:
- Auto-detect your channel ID
- Save it to `config.py`
- Start monitoring for fresher jobs

## Configuration

Edit `config.py` to customize:

- **KEYWORDS** - Search terms (fresher, degree types, roles)
- **LOCATIONS** - Cities to search (Hyderabad, Telangana, etc.)
- **CHECK_INTERVAL_MINUTES** - How often to check (default: 5 min)
- **MIN_MATCH_SCORE** - Minimum relevance score (0-100)
- **MAX_JOBS_PER_CYCLE** - Max jobs per check (prevents spam)

## Files

- `bot.py` - Main bot logic, cycling, and Telegram integration
- `config.py` - Configuration (keywords, locations, bot token)
- `scraper.py` - Web scraper for all job sources
- `sender.py` - Formats and sends jobs to Telegram
- `seen_jobs.json` - Tracks posted jobs (no duplicates)
- `bot.log` - Logs all activity

## Deployment Options

### Local Machine
```bash
python bot.py
```

### GitHub Actions (24/7)
```yaml
name: Fresher Jobs Bot
on:
  schedule:
    - cron: '*/5 * * * *'  # Every 5 minutes
jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run bot
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
        run: python bot.py
```

### Heroku (24/7)
```
heroku login
heroku create degree-jobs-fresher-hyd
git push heroku main
heroku config:set BOT_TOKEN=xxxx CHAT_ID=xxxx
```

### Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]
```

## Logs

Check `bot.log` for activity:
```bash
tail -f bot.log
```

## Support

Bot runs 24/7 with:
- Auto-recovery on network errors
- Duplicate prevention (tracks last 5000 jobs)
- Rate limiting (1-2 sec delays between requests)
- Organized logging with timestamps

---

**Channel:** Degree Jobs Fresher-Hyd
**Updated:** 2026-03-12
**Language:** Python 3.9+
