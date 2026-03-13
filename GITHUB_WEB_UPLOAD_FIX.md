# 🔧 GitHub Web Upload - Fix for requirements.txt Error

## Problem
GitHub Actions can't find `requirements.txt`. You can't push via command line from your laptop.

## Solution
Upload files via GitHub web interface (no git command needed!)

---

## Step 1: Get the Updated Workflow File

**File to upload:** `.github/workflows/bot.yml`

**Location on your laptop:**
```
C:\1 API's work\Test 24\Degree Jobs Fresher\.github\workflows\bot.yml
```

**What's special about this file:**
- It now creates requirements.txt if it doesn't exist
- This is a workaround for the missing file issue
- It will fix the "requirements.txt not found" error

---

## Step 2: Upload via GitHub Web Interface

### 2.1 Go to Your Repository
1. Open: https://github.com/pav715/degree-jobs-fresher-bot
2. You should see the files from your web upload

### 2.2 Go to the Workflows Directory
1. Look for `.github/workflows/` folder
   - If it doesn't exist, you'll need to create it
2. If folder exists, open it
3. Look for `bot.yml` file

### 2.3A: If bot.yml Exists
1. Click on `bot.yml`
2. Click the **pencil icon** (Edit this file)
3. Delete all content
4. Paste the new content (see Step 3 below)
5. Scroll down and click **Commit changes**

### 2.3B: If bot.yml Doesn't Exist (Need to Create Folder)
1. Go to repo main page
2. Click **Add file** → **Create new file**
3. In the filename box, type: `.github/workflows/bot.yml`
4. Paste the new content (see Step 3 below)
5. Scroll down and click **Commit new file**

---

## Step 3: Paste This Content

Copy all of this and paste into the GitHub web editor:

```yaml
name: Degree Jobs Fresher Bot

on:
  schedule:
    - cron: '*/10 * * * *'  # Every 10 minutes (matching config.py)
  workflow_dispatch:  # Manual trigger button

concurrency:
  group: bot-run
  cancel-in-progress: false   # Queue instead of cancel so no run is skipped

jobs:
  run-bot:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
    - name: Checkout repo
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Create requirements.txt (if missing)
      run: |
        if [ ! -f requirements.txt ]; then
          echo "Creating requirements.txt..."
          cat > requirements.txt << 'REQUIREMENTS'
        requests
        beautifulsoup4
        lxml
        REQUIREMENTS
        fi
        cat requirements.txt

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run bot
      env:
        BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
        CHAT_ID: ${{ secrets.CHAT_ID }}
        PYTHONIOENCODING: utf-8
        PYTHONUTF8: '1'
      run: python bot.py

    - name: Save state files back to repo
      run: |
        git config user.name "github-actions[bot]"
        git config user.email "github-actions[bot]@users.noreply.github.com"
        git pull --rebase origin main || true
        git add bot.log seen_jobs.json requirements.txt 2>/dev/null || true
        git diff --staged --quiet || git commit -m "Update bot state and requirements [skip ci]"
        git push || true

    - name: Notify Telegram on failure
      if: failure()
      env:
        BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
        CHAT_ID: ${{ secrets.CHAT_ID }}
      run: |
        curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendMessage" \
          -d "chat_id=${CHAT_ID}" \
          -d "text=❌ Degree Jobs Fresher Bot failed — check GitHub Actions logs" \
          -d "parse_mode=Markdown" || true
```

---

## Step 4: Commit the Change

1. In GitHub web editor, scroll down
2. In the **Commit message** box, type:
   ```
   Fix: Add requirements.txt creation to workflow
   ```
3. Click **Commit changes**

---

## Step 5: Add GitHub Secrets (If Not Done)

1. Go to your repo: https://github.com/pav715/degree-jobs-fresher-bot
2. Click **Settings** (top menu)
3. Click **Secrets and variables** (left sidebar)
4. Click **Actions**
5. Click **New repository secret** (green button)

### Add BOT_TOKEN
- **Name:** `BOT_TOKEN`
- **Value:** `8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0`
- Click **Add secret**

### Add CHAT_ID
- **Name:** `CHAT_ID`
- **Value:** `-1003877235401`
- Click **Add secret**

---

## Step 6: Test the Workflow

1. Go to **Actions** tab (top menu)
2. Click **Degree Jobs Fresher Bot** (left sidebar)
3. Click **Run workflow** (blue button, top right)
4. Click **Run workflow** in dropdown
5. Wait 30 seconds
6. Refresh the page
7. You should see a new run
8. Click on it to see the progress

### What to Expect

**Step 1: Checkout repo** ✅
```
Syncing...
```

**Step 2: Set up Python** ✅
```
Python 3.11 installed
```

**Step 3: Create requirements.txt (if missing)** ✅ NEW!
```
Creating requirements.txt...
requests
beautifulsoup4
lxml
```

**Step 4: Install dependencies** ✅
```
Successfully installed requests beautifulsoup4 lxml
```

**Step 5: Run bot** ✅
```
[2026-03-12 ...] Checking for new fresher jobs...
[2026-03-12 ...] Found X new fresher jobs!
[2026-03-12 ...] Done. Sent X new fresher jobs.
```

**Step 6: Save state files** ✅
```
git commit...
git push...
```

---

## What This Workflow Does (The Fix)

### The Magic Step
```yaml
- name: Create requirements.txt (if missing)
  run: |
    if [ ! -f requirements.txt ]; then
      echo "Creating requirements.txt..."
      cat > requirements.txt << 'REQUIREMENTS'
    requests
    beautifulsoup4
    lxml
    REQUIREMENTS
    fi
    cat requirements.txt
```

**Translation:**
1. Check if `requirements.txt` exists
2. If it doesn't exist, CREATE it
3. Put the dependencies in it
4. Print it to verify

**Why this works:**
- If requirements.txt is on GitHub → uses it
- If requirements.txt is missing → creates it
- Either way, `pip install` succeeds! ✅

---

## Step 7: Verify Success

### On GitHub
1. Go to Actions tab
2. Click the workflow run
3. All steps should be green ✅
4. No red X ❌

### In Telegram
1. Open **Degree Jobs Fresher-Hyd** channel
2. New jobs should appear if any were found

### In bot.log
1. Go to repo main page
2. Find `bot.log` file
3. Click to view
4. Should see execution log with timestamps

---

## If It Still Fails

### Check the Error Message
1. Go to **Actions** tab
2. Click the failed run
3. Scroll to **Run bot** step
4. Click to expand
5. Look for error details

### Common Issues

**Issue: "Still getting requirements.txt error"**
- The workflow file might not have been updated
- Verify the workflow file on GitHub has the new "Create requirements.txt" step
- If not, re-upload it

**Issue: "ImportError: No module named 'requests'"**
- This means pip install didn't run properly
- Check the "Install dependencies" step logs
- Should say "Successfully installed..."

**Issue: "BOT_TOKEN not recognized"**
- GitHub Secrets weren't added properly
- Go to Settings → Secrets and verify both are there
- Make sure they're visible (should show as dots ••••)

**Issue: "No jobs found" (success, but no Telegram message)**
- This is normal! Bot runs successfully but found no new jobs
- Check bot.log to see details
- Next run in 10 minutes might find jobs

---

## Success Checklist

- [ ] Workflow file uploaded to GitHub (`.github/workflows/bot.yml`)
- [ ] Workflow file has "Create requirements.txt" step
- [ ] BOT_TOKEN secret added
- [ ] CHAT_ID secret added
- [ ] Actions tab shows successful runs (green ✅)
- [ ] No "requirements.txt not found" error
- [ ] bot.log shows execution logs
- [ ] Jobs appear in Telegram (if any were found)

---

## Timeline After Upload

| Step | Time | What Happens |
| --- | --- | --- |
| Upload workflow | Now | Workflow file on GitHub |
| Add secrets | 2 min | BOT_TOKEN & CHAT_ID ready |
| Manual trigger | 3 min | Click "Run workflow" |
| First run | 5-10 min | Bot executes |
| Results | 10+ min | Jobs in Telegram (if found) |

---

## You're Almost There! 🎯

This workflow file with the "Create requirements.txt" step is the key.

Once you upload it via GitHub web interface:
1. Workflow will create requirements.txt automatically
2. No more "file not found" error
3. Bot will run successfully
4. You'll have jobs in Telegram

Just a few clicks on GitHub and you're done! ✅

