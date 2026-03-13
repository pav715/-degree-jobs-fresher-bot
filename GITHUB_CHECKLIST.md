# GitHub Setup - Interactive Checklist

## Phase 1: Before You Start

### Prerequisites
- [ ] GitHub account created (or will create now)
- [ ] Windows/Mac/Linux with Command Prompt/Terminal
- [ ] Git installed (or will download)
- [ ] Bot folder: `C:\1 API's work\Test 24\Degree Jobs Fresher`
- [ ] All bot files present (bot.py, config.py, etc.)
- [ ] Telegram channel created: `Degree Jobs Fresher-Hyd`
- [ ] Bot is admin in Telegram channel
- [ ] BOT_TOKEN ready: `8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0`
- [ ] CHAT_ID ready: `-1003877235401`

---

## Phase 2: Setup (Steps 1-3)

### STEP 1: GitHub Account
- [ ] Open https://github.com
- [ ] Click Sign up
- [ ] Fill email, password, username
- [ ] Click Create account
- [ ] Verify email (click link in email)
- [ ] **Confirm:** Can log in to GitHub ✅

### STEP 2: Create Repository
- [ ] Log in to GitHub
- [ ] Click **+** icon (top right)
- [ ] Click **New repository**
- [ ] Repository name: `degree-jobs-fresher-bot`
- [ ] Description: `Telegram bot for fresher jobs in Hyderabad & Telangana`
- [ ] Choose **Public**
- [ ] Click **Create repository**
- [ ] **Copy URL:** `https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git`
- [ ] **Save this URL somewhere safe**

### STEP 3: Prepare Local Machine
- [ ] Open Command Prompt
- [ ] Run: `git --version`
- [ ] **Confirm:** Git is installed (or download from git-scm.com)
- [ ] Navigate to: `cd "C:\1 API's work\Test 24\Degree Jobs Fresher"`
- [ ] Run: `ls -la`
- [ ] **Confirm:** See bot.py, config.py, scraper.py, etc.

---

## Phase 3: Push Code (Steps 4-6)

### STEP 4: Initialize Git
In Command Prompt (in bot folder):
- [ ] Run: `git init`
- [ ] Run: `git add .`
- [ ] Run: `git commit -m "Initial commit: Degree Jobs Fresher Bot"`
- [ ] **Confirm:** See message about 9 files changed

### STEP 5: Connect to GitHub
- [ ] Run: `git remote add origin https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git`
  - **Replace YOUR_USERNAME with your GitHub username!**
- [ ] Run: `git remote -v`
- [ ] **Confirm:** See two lines showing fetch and push URLs
- [ ] Run: `git branch -M main`

### STEP 6: Push to GitHub
- [ ] Run: `git push -u origin main`
- [ ] **When asked for password:**
  - [ ] Get Personal Access Token from: https://github.com/settings/tokens
  - [ ] Click: Generate new token (classic)
  - [ ] Name: `bot-token`
  - [ ] Expiration: 90 days
  - [ ] Scopes: Check `repo` and `workflow`
  - [ ] Click: Generate token
  - [ ] **COPY the token immediately** (you won't see it again!)
- [ ] Paste token as password
- [ ] **Confirm:** See success message about branch main → main

---

## Phase 4: Automation (Steps 7-8)

### STEP 7: Create Workflow File
- [ ] Run: `mkdir -p .github/workflows`
- [ ] Create file: `.github/workflows/bot.yml`
  - [ ] Use Notepad or VS Code
  - [ ] Paste entire YAML content from GITHUB_DETAILED_GUIDE.md (STEP 7.3)
  - [ ] Save file
- [ ] **Confirm:** File exists at `.github/workflows/bot.yml`

### STEP 8: Push Workflow
- [ ] Run: `git add .github/workflows/bot.yml`
- [ ] Run: `git commit -m "Add GitHub Actions workflow"`
- [ ] Run: `git push`
- [ ] **Confirm:** See message about commit

---

## Phase 5: Configuration (Step 9)

### STEP 9: Add GitHub Secrets
- [ ] Open your GitHub repo in browser
- [ ] Click: **Settings** (top menu)
- [ ] Click: **Secrets and variables** (left sidebar)
- [ ] Click: **Actions**
- [ ] Click: **New repository secret**
  - [ ] Name: `BOT_TOKEN`
  - [ ] Value: `8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0`
  - [ ] Click: **Add secret**
- [ ] Click: **New repository secret** (again)
  - [ ] Name: `CHAT_ID`
  - [ ] Value: `-1003877235401`
  - [ ] Click: **Add secret**
- [ ] **Confirm:** See both secrets listed (as dots: •••••)

---

## Phase 6: Testing (Step 10)

### STEP 10: Test Workflow
- [ ] Open your GitHub repo in browser
- [ ] Click: **Actions** (top menu)
- [ ] Click: **Degree Jobs Fresher Bot** (left sidebar)
- [ ] Click: **Run workflow** (blue button, top right)
- [ ] Click: **Run workflow** (in dropdown)
- [ ] Wait 30 seconds and refresh page
- [ ] Click the new run that appears
- [ ] **Check all steps:**
  - [ ] Checkout code ✅ (green)
  - [ ] Set up Python ✅ (green)
  - [ ] Install dependencies ✅ (green)
  - [ ] Run bot ✅ (green)
  - [ ] Commit updates ✅ (green)
- [ ] **If all green:** SUCCESS! ✅
- [ ] Open Telegram: **Degree Jobs Fresher-Hyd**
- [ ] **Confirm:** See new jobs posted (if any found)

---

## Phase 7: Monitoring (Steps 11-12)

### STEP 11: Automatic Scheduling
- [ ] Bot will now run every 10 minutes automatically
- [ ] No action needed from you
- [ ] GitHub servers handle everything
- [ ] Your PC can be OFF
- [ ] **Monitoring:**
  - [ ] Go to repo → **Actions** tab
  - [ ] See new runs appearing every 10 minutes
  - [ ] Green ✅ = successful run
  - [ ] Red ❌ = check logs for error

### STEP 12: Monitor Telegram
- [ ] Open Telegram app/web
- [ ] Go to: **Degree Jobs Fresher-Hyd** channel
- [ ] **Watch for:** New jobs appearing every 10 minutes
- [ ] **Each job shows:**
  - [ ] Job title (e.g., "Tax Assistant Fresher")
  - [ ] Company name
  - [ ] Location (Hyderabad/Telangana)
  - [ ] Job source (LinkedIn, Naukri, etc.)
  - [ ] Apply link

---

## After Setup: Maintenance

### To Update Keywords/Config
- [ ] Edit `config.py` locally (on your PC)
- [ ] Run: `git add .`
- [ ] Run: `git commit -m "Updated keywords"`
- [ ] Run: `git push`
- [ ] Done! GitHub uses new config next run

### To Check Bot Status
- [ ] Go to: `https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot/actions`
- [ ] See all workflow runs
- [ ] Click any run to see logs
- [ ] Shows what was searched, what was posted, any errors

### To Check Bot Logs
- [ ] Go to repo on GitHub
- [ ] Click on `bot.log`
- [ ] See all activity (searches, jobs found, posts, errors)

### To Check Posted Jobs
- [ ] Go to repo on GitHub
- [ ] Click on `seen_jobs.json`
- [ ] See all jobs that were posted (to prevent duplicates)

---

## Success Indicators ✅

After all steps, you should see:

### On GitHub
- [ ] Repository exists with all your code
- [ ] `.github/workflows/bot.yml` file present
- [ ] Both secrets listed (BOT_TOKEN, CHAT_ID)
- [ ] Multiple green ✅ workflow runs
- [ ] `bot.log` updated with recent runs
- [ ] `seen_jobs.json` growing with posted jobs

### On Telegram
- [ ] Jobs appearing in **Degree Jobs Fresher-Hyd** channel
- [ ] New jobs posted every 10 minutes
- [ ] Job info includes: title, company, location, apply link
- [ ] Focus on TAX-related jobs (primary keyword)

### On Your PC
- [ ] Nothing needed!
- [ ] Can be OFF 24/7
- [ ] No manual work required
- [ ] Just monitor results

---

## Troubleshooting Checklist

### If GitHub Workflow Shows RED ❌

- [ ] Click the red run to see error message
- [ ] **Common issues:**
  - [ ] Missing secrets? Go to Step 9, verify BOT_TOKEN and CHAT_ID exist
  - [ ] Wrong Python version? Check workflow file uses `python-version: '3.9'`
  - [ ] Git push error? Verify GitHub user email: `git config --global user.email`

- [ ] **Fix:** Edit the file causing error
- [ ] [ ] Run: `git add .`
- [ ] [ ] Run: `git commit -m "Fix: issue description"`
- [ ] [ ] Run: `git push`
- [ ] [ ] Workflow auto-retries next scheduled time

### If Jobs Not Posting to Telegram

- [ ] Check CHAT_ID is correct: `-1003877235401`
- [ ] Verify bot is admin in Telegram channel
- [ ] Check bot has permission to post messages
- [ ] View workflow logs to see if jobs were found
- [ ] **If no jobs found:** Check if search terms are matching available jobs

### If "Authentication Failed" During git push

- [ ] Get new Personal Access Token: https://github.com/settings/tokens
- [ ] Make sure token has `repo` and `workflow` scopes
- [ ] Paste full token (including letters and numbers)
- [ ] Don't use GitHub password, only token

---

## Final Checklist ✅

Before declaring "DONE":

### GitHub Setup
- [ ] Account created and verified
- [ ] Repository created and code pushed
- [ ] Workflow file created and pushed
- [ ] Secrets added (BOT_TOKEN, CHAT_ID)
- [ ] Test run completed successfully (all green ✅)

### Bot Status
- [ ] Bot runs every 10 minutes (visible in Actions)
- [ ] No recent errors (no red ❌)
- [ ] Jobs posting to Telegram (check channel)

### Automation
- [ ] PC not required to be on
- [ ] No manual restarts needed
- [ ] GitHub runs bot automatically
- [ ] Everything self-updating

### Documentation
- [ ] Understand how to update code (git push)
- [ ] Know where to check logs (Actions tab)
- [ ] Know how to monitor results (Telegram channel)

---

## 🎉 COMPLETE!

When everything is checked:
- ✅ Your bot is running 24/7 on GitHub
- ✅ Jobs posting to Telegram automatically
- ✅ No PC needed
- ✅ Free forever
- ✅ Professional setup

---

## Support Resources

If you get stuck:
1. **GITHUB_DETAILED_GUIDE.md** - Full explanation with examples
2. **COPY_PASTE_COMMANDS.md** - All commands ready to copy
3. **GITHUB_STEP_BY_STEP.md** - Detailed walkthrough
4. **GITHUB_VISUAL_FLOWCHART.md** - Visual overview
5. GitHub Docs: https://docs.github.com
6. GitHub Actions Docs: https://docs.github.com/en/actions

---

**Ready? Start with Step 1 and follow the checklist!** 🚀
