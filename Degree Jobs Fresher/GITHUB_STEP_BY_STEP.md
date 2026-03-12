# GitHub Setup - Complete Step-by-Step Guide

## 🎯 Goal
Push your Degree Jobs Fresher Bot to GitHub and set it to run **24/7 automatically** every 10 minutes.

---

# STEP 1: Create GitHub Account (if you don't have one)

### 1.1 Go to GitHub
- Open browser: https://github.com
- Click **Sign up**

### 1.2 Fill Details
- **Username:** (anything, e.g., `your-name`)
- **Email:** Your email address
- **Password:** Create strong password
- Click **Create account**

### 1.3 Verify Email
- GitHub sends verification email
- Click link in email
- Done! ✅

---

# STEP 2: Create Repository on GitHub

### 2.1 After Login, Click **+** (top right)
- Click **+** icon (top right corner)
- Click **New repository**

### 2.2 Fill Repository Details
**Repository name:**
```
degree-jobs-fresher-bot
```

**Description:** (optional)
```
Telegram bot for fresher jobs in Hyderabad & Telangana
```

**Public or Private:**
- Choose **Public** (easier to share)

**Scroll down → Click "Create repository"**

### 2.3 Copy Repository URL
After creation, you'll see this page:

```
https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git
```

**Copy this URL** (you'll need it soon)

---

# STEP 3: Prepare Your Local Code

### 3.1 Check If Git Is Installed
Open **Command Prompt** or **Terminal**:

```bash
git --version
```

If it shows version, Git is installed ✅

If not, download from: https://git-scm.com/

### 3.2 Navigate to Bot Folder
```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
```

### 3.3 Check Files Are There
```bash
ls -la
```

You should see:
- bot.py
- config.py
- scraper.py
- sender.py
- requirements.txt
- README.md
- bot.log
- seen_jobs.json

---

# STEP 4: Initialize Git in Your Folder

### 4.1 Initialize Git Repository
```bash
git init
```

Output:
```
Initialized empty Git repository in C:\1 API's work\Test 24\Degree Jobs Fresher\.git
```

### 4.2 Add All Files
```bash
git add .
```

This stages all files for upload.

### 4.3 Create First Commit
```bash
git commit -m "Initial commit: Degree Jobs Fresher Bot"
```

Output:
```
[main (root-commit) abc1234] Initial commit: Degree Jobs Fresher Bot
 9 files changed, 500 insertions(+)
```

---

# STEP 5: Connect to GitHub Repository

### 5.1 Add Remote Origin
Replace `YOUR_USERNAME` with your GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git
```

Example:
```bash
git remote add origin https://github.com/john-smith/degree-jobs-fresher-bot.git
```

### 5.2 Verify Connection
```bash
git remote -v
```

Should show:
```
origin  https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git (fetch)
origin  https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git (push)
```

### 5.3 Rename Branch to Main (if needed)
```bash
git branch -M main
```

---

# STEP 6: Push Code to GitHub

### 6.1 First Time Push
```bash
git push -u origin main
```

It will ask for **GitHub credentials**:
- **Username:** Your GitHub username
- **Password:** Use a **Personal Access Token** (not your password)

### 6.2 Get Personal Access Token
If you don't have one, create it:

1. Go to: https://github.com/settings/tokens
2. Click **Generate new token (classic)**
3. Fill details:
   - **Token name:** `bot-token`
   - **Expiration:** 90 days (or No expiration)
   - **Select scopes:** Check `repo` and `workflow`
4. Click **Generate token**
5. **Copy the token** (you won't see it again!)

### 6.3 Paste Token as Password
When git asks for password during `git push`:
- Paste the token you copied
- Press Enter

### 6.4 Success Message
```
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Writing objects: 100% (9/9), 2.50 KiB | 2.50 MiB/s, done.
Total 9 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git
 * [new branch]      main -> main
Branch 'main' set to track remote branch 'main' from 'origin'.
```

✅ **Code is now on GitHub!**

---

# STEP 7: Create GitHub Actions Workflow

### 7.1 Create Folder Structure
In your bot folder, create these folders:
```
.github/workflows/
```

**Command:**
```bash
mkdir -p .github/workflows
```

### 7.2 Create Workflow File
Create file: `.github/workflows/bot.yml`

**Content to paste:**
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

    - name: Run bot
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

### 7.3 Save the File
Save this file in: `.github/workflows/bot.yml`

Your folder structure should now be:
```
Degree Jobs Fresher/
├── .github/
│   └── workflows/
│       └── bot.yml          ← NEW FILE
├── bot.py
├── config.py
├── ...
```

---

# STEP 8: Push Workflow File to GitHub

### 8.1 Add Workflow File
```bash
git add .github/workflows/bot.yml
```

### 8.2 Commit
```bash
git commit -m "Add GitHub Actions workflow"
```

### 8.3 Push to GitHub
```bash
git push
```

✅ **Workflow is now on GitHub!**

---

# STEP 9: Add GitHub Secrets

### 9.1 Go to Repository Settings
1. Open your GitHub repo: `https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot`
2. Click **Settings** (top menu)
3. Click **Secrets and variables** (left sidebar)
4. Click **Actions**

### 9.2 Add BOT_TOKEN Secret

1. Click **New repository secret** (green button)
2. **Name:** `BOT_TOKEN`
3. **Value:** `8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0`
4. Click **Add secret**

✅ BOT_TOKEN added!

### 9.3 Add CHAT_ID Secret

1. Click **New repository secret** (green button)
2. **Name:** `CHAT_ID`
3. **Value:** `-1003877235401`
4. Click **Add secret**

✅ CHAT_ID added!

### 9.4 Verify Both Secrets
You should now see:
```
BOT_TOKEN  •••••••••
CHAT_ID    •••••••••
```

---

# STEP 10: Test the Workflow

### 10.1 Go to Actions Tab
1. Open your GitHub repo
2. Click **Actions** (top menu)

### 10.2 Select Your Workflow
1. Left sidebar: Click **Degree Jobs Fresher Bot**
2. You should see workflow listed

### 10.3 Run Manually
1. Click **Run workflow** (top right)
2. Click **Run workflow** (in dropdown)
3. Wait 30 seconds...

### 10.4 Check Execution
1. Refresh page
2. You'll see a new run appear
3. Click on it to see details
4. Watch the steps execute:
   - ✅ Checkout code
   - ✅ Set up Python
   - ✅ Install dependencies
   - ✅ Run bot
   - ✅ Commit updates

### 10.5 Check Success
- If all steps show ✅ green, it worked!
- Check your Telegram channel - jobs should be posted!

---

# STEP 11: Automatic Scheduling

Now the bot will **automatically run**:

### 11.1 How It Works
- GitHub Actions runs the workflow **every 10 minutes**
- No action needed from you
- Bot keeps searching for jobs
- Posts to Telegram automatically

### 11.2 Check Status Anytime
1. Go to repo → **Actions** tab
2. See all runs (green ✅ = success)
3. Click any run to see logs

### 11.3 View Run History
- Shows date/time each run happened
- Shows if jobs were found
- Shows any errors

---

# STEP 12: Monitor Telegram Channel

### 12.1 Open Telegram
1. Open Telegram app/web
2. Go to **Degree Jobs Fresher-Hyd** channel
3. Watch for new jobs appearing every 10 minutes

### 12.2 Jobs Should Show Like:
```
📌 Associate Engineer (Fresher)
Company: Wipro
Location: Hyderabad

🔗 Apply Now
```

---

# ✅ You're Done!

## Summary of What You Did

| Step | What | Status |
| :--- | :--- | :--- |
| 1 | Created GitHub account | ✅ |
| 2 | Created repository | ✅ |
| 3 | Prepared local code | ✅ |
| 4 | Initialized Git | ✅ |
| 5 | Connected to GitHub | ✅ |
| 6 | Pushed code | ✅ |
| 7 | Created workflow | ✅ |
| 8 | Pushed workflow | ✅ |
| 9 | Added secrets | ✅ |
| 10 | Tested manually | ✅ |
| 11 | Enabled automation | ✅ |
| 12 | Monitor channel | ✅ |

---

# 🎉 Result

✅ **Bot runs 24/7 automatically**
✅ **Every 10 minutes** it checks for jobs
✅ **Posts to Telegram** instantly
✅ **No local machine needed** (runs on GitHub servers)
✅ **Free** (GitHub free tier)
✅ **Version control** (all changes tracked)

---

# 📝 Common Commands Going Forward

### Update Code (after making changes locally)
```bash
git add .
git commit -m "Description of changes"
git push
```

### View Recent Commits
```bash
git log --oneline -5
```

### Check Workflow Status
Go to: `https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot/actions`

### View Bot Logs
In GitHub repo:
1. Go to `bot.log`
2. Click pencil icon
3. See recent runs

---

# 🆘 Troubleshooting

### Workflow Won't Run
- Check **Actions** tab
- Look for red ❌ errors
- Verify secrets are set correctly
- Check bot.log for details

### Jobs Not Posting
- Verify CHAT_ID is correct
- Check bot has admin in Telegram channel
- View workflow logs to see errors

### Personal Access Token Issues
- Create new token: https://github.com/settings/tokens
- Copy full token (won't show again)
- Use as password during git push

---

**🎯 That's it! Your bot is now live on GitHub and running 24/7!** 🚀
