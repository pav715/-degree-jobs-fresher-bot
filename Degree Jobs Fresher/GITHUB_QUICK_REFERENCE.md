# GitHub Quick Reference - Copy/Paste Commands

## 📋 All Commands You Need

### STEP 1: Navigate to Bot Folder
```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
```

---

### STEP 2: Check Git Installation
```bash
git --version
```

If it shows a version, Git is installed ✅

---

### STEP 3: Initialize Git
```bash
git init
```

---

### STEP 4: Add All Files
```bash
git add .
```

---

### STEP 5: Create First Commit
```bash
git commit -m "Initial commit: Degree Jobs Fresher Bot"
```

---

### STEP 6: Add GitHub Remote (REPLACE YOUR_USERNAME)
```bash
git remote add origin https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git
```

**Example:**
```bash
git remote add origin https://github.com/john-smith/degree-jobs-fresher-bot.git
```

---

### STEP 7: Rename Branch to Main
```bash
git branch -M main
```

---

### STEP 8: Push Code to GitHub
```bash
git push -u origin main
```

When asked for password, **paste your Personal Access Token** (from Step 9.2 in full guide)

---

### STEP 9: Create Workflow Folder
```bash
mkdir -p .github/workflows
```

---

### STEP 10: Add Workflow File
Create file: `.github/workflows/bot.yml`

**Paste this content:**
```yaml
name: Degree Jobs Fresher Bot

on:
  schedule:
    - cron: '*/10 * * * *'
  workflow_dispatch:

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

---

### STEP 11: Push Workflow to GitHub
```bash
git add .github/workflows/bot.yml
```

```bash
git commit -m "Add GitHub Actions workflow"
```

```bash
git push
```

---

## 🔐 GitHub Secrets Setup

### Secret 1: BOT_TOKEN
- **Name:** `BOT_TOKEN`
- **Value:** `8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0`

### Secret 2: CHAT_ID
- **Name:** `CHAT_ID`
- **Value:** `-1003877235401`

**Where to add:**
1. GitHub repo → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add each secret

---

## 🧪 Test Workflow

1. Go to: `https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot`
2. Click **Actions** tab
3. Click **Degree Jobs Fresher Bot** workflow
4. Click **Run workflow** → **Run workflow**
5. Wait and watch execution

---

## 📱 Check Telegram

Open your **Degree Jobs Fresher-Hyd** channel and wait for jobs to appear!

---

## 🔄 Future Updates

After setup, to make changes:

```bash
# Make changes to files locally
# Then:

git add .
git commit -m "Your description here"
git push
```

GitHub will automatically use the new code!

---

## 📊 Monitor Bot

**View workflow runs:**
`https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot/actions`

**View bot logs:**
`https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot/blob/main/bot.log`

---

## ⚠️ One-Time Setup Items

These you only do ONCE:

1. ✅ Create GitHub account
2. ✅ Create repository
3. ✅ Initialize git locally
4. ✅ Create workflow file
5. ✅ Add secrets

**After that:** Just use `git add . → git commit → git push` for any updates!

---

## 🎯 That's All You Need!

Everything above is copy-paste ready.

Just replace `YOUR_USERNAME` with your GitHub username and follow the steps in order!

✅ **Result:** 24/7 Automated Bot 🚀
