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

      # Check if we have BOT_TOKEN and CHAT_ID
      if not config.BOT_TOKEN or not config.CHAT_ID:
          log("ERROR: BOT_TOKEN or CHAT_ID not set. Please add to GitHub Secrets.")
          log(f"  BOT_TOKEN set: {bool(config.BOT_TOKEN)}")
          log(f"  CHAT_ID set: {bool(config.CHAT_ID)}")
          return

      log(f"✅ Bot configured: BOT_TOKEN and CHAT_ID loaded from environment")

      # Load seen jobs (prevents duplicates)
      seen = load_seen()
      log(f"Loaded {len(seen)} previously seen jobs (no duplicates).")

      # First run immediately (don't wait for interval)
      run_cycle(seen)

      interval = config.CHECK_INTERVAL_MINUTES * 60

      # Main loop - runs forever
      while True:
          next_check = datetime.now().strftime("%H:%M:%S")
          log(f"Sleeping {config.CHECK_INTERVAL_MINUTES} min... (next check around {next_check})")
          time.sleep(interval)
          run_cycle(seen)


  def run_cycle(seen):
      """Run one complete job search and posting cycle."""
      log(f"Checking for new fresher jobs... ({len(config.KEYWORDS)} keywords x {len(config.LOCATIONS)} locations)")
      try:
          jobs = fetch_all_jobs()
      except Exception as e:
          log(f"Scrape error: {e}")
          return

      # Filter out already-seen jobs
      new_jobs = [j for j in jobs if j["id"] not in seen]

      if not new_jobs:
          log(f"No new jobs found. Total tracked: {len(seen)}")
          return

      log(f"Found {len(new_jobs)} new fresher jobs! Sending to Telegram...")

      sent = 0
      for job in new_jobs:
          try:
              ok = send_job(job)
              if ok:
                  seen.add(job["id"])
                  sent += 1
                  log(f"  ✅ Sent: [{job['source']}] {job['title']} @ {job['company']} | {job['location']}")
              else:
                  log(f"  ❌ Failed to send: {job['title']}")
          except Exception as e:
              log(f"  Error sending job: {e}")

      save_seen(seen)
      log(f"Done. Sent {sent} new fresher jobs. Total tracked: {len(seen)}")


  if __name__ == "__main__":
      main()
