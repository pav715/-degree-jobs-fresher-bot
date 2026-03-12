# Degree Jobs Fresher Bot - Setup Guide

## Step 1: Create Telegram Channel

1. Open **Telegram Desktop** or **Web**
2. Click **+ New Channel**
3. Name: `Degree Jobs Fresher-Hyd`
4. Choose **Private Channel**
5. Click **Create**

## Step 2: Add Bot as Admin

1. Go to your channel settings
2. Click **Add Members** / **Manage Channel**
3. Search for: `@USTaxjobs_bot`
4. Add as **Admin**
5. Give permission: **Post messages**
6. Save

## Step 3: Send Test Message

1. Click in your channel
2. Send a test message (e.g., "Testing")
3. This ensures the bot can connect

## Step 4: Get Your Channel ID

### Method 1: Browser (Easiest)

1. Open this link in your browser:
   ```
   https://api.telegram.org/bot8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0/getUpdates
   ```

2. Look for this in the page:
   ```json
   "chat":{"id":-1001234567890, ...}
   ```

3. Copy the **negative number** (e.g., `-1001234567890`)

### Method 2: Telegram Bot Debugger

1. Use @userinfobot in Telegram
2. Forward a message from your channel
3. It shows the channel ID

## Step 5: Update config.py

1. Open `config.py`
2. Find this line:
   ```python
   CHAT_ID = os.environ.get("CHAT_ID", "-1001234567890")
   ```

3. Replace `-1001234567890` with your actual channel ID
4. Save the file

## Step 6: Run the Bot

```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
python bot.py
```

## Expected Output

```
[2026-03-12 17:40:02] ============================================================
[2026-03-12 17:40:02]   Degree Jobs Fresher — Hyderabad & Telangana
[2026-03-12 17:40:02]   Check interval: every 10 minutes
[2026-03-12 17:40:02] ============================================================
[2026-03-12 17:40:02] Loaded 0 previously seen jobs
[2026-03-12 17:40:02] Checking for new fresher jobs...
```

Then it will start searching and posting jobs to your channel every 10 minutes!

## Troubleshooting

**Problem:** `Cannot start without CHAT_ID`
- **Solution:** Double-check your CHAT_ID in config.py. It should start with `-100`

**Problem:** `Telegram setup error`
- **Solution:** Make sure bot is added as Admin to the channel

**Problem:** No jobs appearing
- **Solution:** Check that bot has **Post messages** permission

## Support

Check logs:
```bash
tail -f bot.log
```

---

**Bot Token Used:** `8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0` (Shared with @USTaxjobs_bot)
**Check Interval:** 10 minutes
**Locations:** Hyderabad & Telangana Only
**Target:** Freshers (0-1 years experience)
