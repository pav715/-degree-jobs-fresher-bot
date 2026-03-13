# GitHub Setup for Degree Jobs Fresher Bot

## Why GitHub?

- **Version Control** - Track all changes
- **24/7 Automation** - GitHub Actions runs bot automatically
- **No Local Machine** - Don't need your PC running
- **Backup** - Safe cloud storage

---

## Step 1: Create GitHub Repository

### 1.1 Create New Repo on GitHub
1. Go to [github.com](https://github.com)
2. Click **+** → **New repository**
3. Name: `degree-jobs-fresher-bot`
4. Description: `Telegram bot for fresher jobs in Hyderabad & Telangana`
5. Choose **Public** (easier) or **Private**
6. Click **Create repository**

### 1.2 Get Your Repo URL
Copy this: `https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git`

---

## Step 2: Push Code to GitHub

### 2.1 Initialize Git in Bot Folder
```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
git init
git add .
git commit -m "Initial commit: Degree Jobs Fresher Bot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git
git push -u origin main
```

### 2.2 What Gets Pushed
```
✅ bot.py
✅ config.py
✅ scraper.py
✅ sender.py
✅ requirements.txt
✅ README.md
✅ bot.log (updates with new runs)
✅ seen_jobs.json (tracks posted jobs)
```

---

## Step 3: GitHub Actions - Run Bot 24/7

### 3.1 Create Workflow File
Create file: `.github/workflows/bot.yml`

```yaml
name: Degree Jobs Fresher Bot

on:
  schedule:
    - cron: '*/10 * * * *'  # Every 10 minutes
  workflow_dispatch:  # Manual trigger button

jobs:
  run-bot:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run bot once
      env:
        BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
        CHAT_ID: ${{ secrets.CHAT_ID }}
      run: python bot.py

    - name: Commit updates
      run: |
        git config --local user.email "bot@github.com"
        git config --local user.name "GitHub Bot"
        git add bot.log seen_jobs.json
        git commit -m "Bot run: $(date)" || true
        git push
```

Save as: `.github/workflows/bot.yml`

---

## Step 4: Add GitHub Secrets

### 4.1 Go to Repository Settings
1. GitHub repo → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**

### 4.2 Add BOT_TOKEN
- Name: `BOT_TOKEN`
- Value: `8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0`
- Click **Add secret**

### 4.3 Add CHAT_ID
- Name: `CHAT_ID`
- Value: `-1003877235401` (your channel ID)
- Click **Add secret**

✅ Both secrets added!

---

## Step 5: Test the Workflow

### 5.1 Manual Trigger
1. Go to repo → **Actions** tab
2. Select **Degree Jobs Fresher Bot** workflow
3. Click **Run workflow** → **Run workflow**
4. Watch it run!

### 5.2 Check Logs
- Click on the running job
- See real-time output
- Check if jobs posted to Telegram

---

## Step 6: Automate (Every 10 Minutes)

The workflow runs automatically:
- **Every 10 minutes** (via cron schedule)
- **24/7** (GitHub runs it for you)
- **No local machine needed**

Check status:
1. Go to repo → **Actions** tab
2. See all runs (green ✅ = success)
3. Click any run to see logs

---

## File Structure on GitHub

```
degree-jobs-fresher-bot/
├── .github/
│   └── workflows/
│       └── bot.yml              (Automation config)
├── bot.py                        (Main bot)
├── config.py                     (Settings + Keywords)
├── scraper.py                    (Job scraper)
├── sender.py                     (Telegram sender)
├── requirements.txt              (Dependencies)
├── README.md                     (Documentation)
├── GITHUB_SETUP.md              (This file)
├── bot.log                       (Activity log - updated by bot)
├── seen_jobs.json               (Posted jobs - updated by bot)
└── .gitignore                   (Exclude sensitive files)
```

---

## Step 7: Optional - Add .gitignore

Create file: `.gitignore`

```
# Environment
.env
*.pyc
__pycache__/

# Logs (optional - can track to see history)
# bot.log

# IDE
.vscode/
.idea/
*.swp
```

---

## Troubleshooting

### Bot doesn't run on schedule
- Check **Actions** tab → Workflow runs
- Check for red ❌ errors
- Verify secrets are set correctly

### Jobs not posting
- Check `bot.log` in latest run
- Verify `CHAT_ID` is correct
- Ensure bot has permission in Telegram channel

### Secrets not working
- Go to **Settings** → **Secrets** → verify both secrets exist
- Check workflow file has correct secret names
- Re-run workflow after updating secrets

---

## Quick Commands

### Push changes to GitHub
```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
git add .
git commit -m "Description of changes"
git push
```

### Pull latest from GitHub
```bash
git pull
```

### View status
```bash
git status
```

---

## Summary

| Step | What | Done? |
| :--- | :--- | :--- |
| Create GitHub Repo | New repo on GitHub | [ ] |
| Push Code | Upload bot code | [ ] |
| Add Secrets | BOT_TOKEN, CHAT_ID | [ ] |
| Create Workflow | .github/workflows/bot.yml | [ ] |
| Test Manual Run | Run workflow once | [ ] |
| Enable Automation | Runs every 10 min | ✅ |

---

## Result: 24/7 Automated Bot

✅ Runs every 10 minutes automatically
✅ Posts fresher jobs to Telegram
✅ No local machine needed
✅ Version control on GitHub
✅ Free (GitHub Actions free tier)

Ready to set up? 🚀
