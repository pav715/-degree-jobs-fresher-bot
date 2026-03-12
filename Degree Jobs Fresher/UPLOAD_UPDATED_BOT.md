# 📤 Upload Updated bot.py (No Welcome Message)

## What Changed
✅ Removed the startup/welcome message
✅ Bot now ONLY posts actual job listings
✅ No welcome message in channel anymore

---

## How to Upload

### Step 1: Open GitHub
Go to: https://github.com/pav715/degree-jobs-fresher-bot

### Step 2: Find bot.py
1. Look for `bot.py` in the root
2. Or inside `Degree Jobs Fresher` folder
3. Click on it

### Step 3: Edit File
1. Click pencil icon (Edit this file)

### Step 4: Replace Content

Delete everything and paste THIS:

```python
"""
Degree Jobs Fresher — Telegram Bot
Runs 24/7, checks every 10 minutes, sends new fresher jobs instantly.
No duplicates. Newest first.
Target: ANY Graduate (All degrees - No B.Tech/M.Tech)
Location: Hyderabad & Telangana Only
Experience: Freshers Only (0-1 years)
Focus: TAX jobs (primary) + All fresher jobs

Features (same as US Tax bot):
✅ Auto-CHAT_ID detection
✅ Duplicate prevention (5000 job history)
✅ Comprehensive logging
✅ Professional message formatting
✅ Error recovery
✅ Rate limiting (2 sec between posts)

Run: python bot.py
"""
import json
import os
import time
import re
import requests
from datetime import datetime
import config
from scraper import fetch_all_jobs
from sender import send_job

SEEN_FILE = "seen_jobs.json"
LOG_FILE  = "bot.log"


# ── Seen jobs tracker ─────────────────────────────────────────────────
def load_seen():
    """Load previously seen job IDs to prevent duplicates."""
    if os.path.exists(SEEN_FILE):
        try:
            with open(SEEN_FILE, "r") as f:
                return set(json.load(f))
        except Exception:
            pass
    return set()


def save_seen(seen_set):
    """Save seen job IDs. Keep only last 5000 to avoid file bloat."""
    data = list(seen_set)[-5000:]
    with open(SEEN_FILE, "w") as f:
        json.dump(data, f)


# ── Logging ───────────────────────────────────────────────────────────
def log(msg):
    """Log message to both console and file with timestamp."""
    ts  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# ── Telegram setup ────────────────────────────────────────────────────
def setup_telegram():
    """Detect Chat ID on first run if not already set."""
    if config.CHAT_ID:
        return True

    log("CHAT_ID not set. Detecting from Telegram updates...")
    try:
        r = requests.get(
            f"https://api.telegram.org/bot{config.BOT_TOKEN}/getUpdates",
            timeout=15
        )
        data = r.json()
        for item in data.get("result", []):
            chat = (
                item.get("channel_post", {}).get("chat")
                or item.get("message", {}).get("chat")
                or {}
            )
            if chat.get("id"):
                chat_id = str(chat["id"])
                config.CHAT_ID = chat_id
                _save_chat_id(chat_id)
                log(f"Chat ID detected and saved: {chat_id} ({chat.get('title','')}")
                return True

        log("No channel found. Add bot as Admin to 'Degree Jobs Fresher-Hyd', send a message, then restart.")
        return False
    except Exception as e:
        log(f"Telegram setup error: {e}")
        return False


def _save_chat_id(chat_id):
    """Write Chat ID into config.py automatically (one-time setup)."""
    try:
        path = os.path.join(os.path.dirname(__file__), "config.py")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = re.sub(
            r'os\.environ\.get\("CHAT_ID",\s*"[^"]*"\)',
            f'os.environ.get("CHAT_ID", "{chat_id}")',
            content, count=1
        )
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception:
        pass


# ── One scrape cycle ──────────────────────────────────────────────────
def run_cycle(seen):
    """Run one complete job search and posting cycle."""
    log(f"Checking for new fresher jobs... ({len(config.KEYWORDS)} keywords x {len(config.LOCATIONS)} locations)")
    try:
        jobs = fetch_all_jobs()
    except Exception as e:
        log(f"Scrape error: {e}")
        return seen, 0

    # Filter out already-seen jobs
    new_jobs = [j for j in jobs if j["id"] not in seen]

    if not new_jobs:
        log(f"No new jobs found. Total tracked: {len(seen)}")
        return seen, 0

    log(f"Found {len(new_jobs)} new fresher jobs! Sending to Telegram...")

    sent = 0
    for job in new_jobs:   # already sorted newest first by scraper
        try:
            ok = send_job(job)
            if ok:
                seen.add(job["id"])
                sent += 1
                log(f"  Sent: [{job['source']}] {job['title']} @ {job['company']} | {job['location']}")
            else:
                log(f"  Failed to send: {job['title']}")
        except Exception as e:
            log(f"  Error sending job: {e}")

    save_seen(seen)
    log(f"Done. Sent {sent} new fresher jobs. Total tracked: {len(seen)}")
    return seen, sent


# ── Main loop ─────────────────────────────────────────────────────────
def main():
    """Main bot loop - runs forever, checks every CHECK_INTERVAL_MINUTES."""
    log("=" * 70)
    log("  Degree Jobs Fresher — Telegram Bot")
    log("  TARGET: Fresher jobs (0-1 years) | FOCUS: TAX jobs (primary)")
    log("  DEGREES: Any (B.A., B.Sc., B.Com., BBA, BCA, B.Ed., BSW, MBA, etc.)")
    log("  LOCATIONS: Hyderabad & Telangana only")
    log(f"  CHECK INTERVAL: Every {config.CHECK_INTERVAL_MINUTES} minutes")
    log("=" * 70)

    # Setup Telegram (auto-detect CHAT_ID if needed)
    if not setup_telegram():
        log("Cannot start without CHAT_ID. Exiting.")
        return

    # Load seen jobs (prevents duplicates)
    seen = load_seen()
    log(f"Loaded {len(seen)} previously seen jobs (no duplicates).")

    # First run immediately (don't wait for interval)
    seen, sent = run_cycle(seen)

    interval = config.CHECK_INTERVAL_MINUTES * 60

    # Main loop - runs forever
    while True:
        next_check = datetime.now().strftime("%H:%M:%S")
        log(f"Sleeping {config.CHECK_INTERVAL_MINUTES} min... (next check around {next_check})")
        time.sleep(interval)
        seen, sent = run_cycle(seen)


if __name__ == "__main__":
    main()
```

### Step 5: Commit
1. Scroll down
2. Message: `Remove welcome message - only post jobs`
3. Click **Commit changes**

---

## What This Does

✅ **Before:** Startup message posted to channel every 10 minutes
❌ **After:** No startup message. Only job listings posted!

---

## Test It

1. Go to **Actions** tab
2. Click **Run workflow**
3. Click **Run workflow** again
4. Wait 30 seconds
5. Refresh
6. Should see green ✅

Now when bot runs, Telegram channel will ONLY show job listings, not welcome messages! 🎯

