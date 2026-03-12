# Next Steps After Uploading to GitHub

## ✅ Code is Now on GitHub!

Your bot folder is now uploaded to:
```
https://github.com/pav715/degree-jobs-fresher-bot
```

---

## 🎯 What's Next: Steps 7-9

### **STEP 7: Create Workflow File (.github/workflows/bot.yml)**

This tells GitHub to run your bot automatically every 10 minutes.

#### 7.1 On Your Local Machine (Command Prompt):

```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
mkdir -p .github/workflows
```

#### 7.2 Create File: `.github/workflows/bot.yml`

Use **Notepad** or **VS Code**:
- Create new file
- Paste this content (below)
- Save as: `.github/workflows/bot.yml`
- Put it in: `.github/workflows/` folder

#### 7.3 Content to Paste:

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

#### 7.4 Push Workflow to GitHub:

```bash
git add .github/workflows/bot.yml
git commit -m "Add GitHub Actions workflow"
git push
```

---

### **STEP 8: Add GitHub Secrets**

The bot needs your BOT_TOKEN and CHAT_ID as secrets.

#### 8.1 Go to Your Repository Settings

1. Open: https://github.com/pav715/degree-jobs-fresher-bot
2. Click **Settings** (top menu)
3. Click **Secrets and variables** (left sidebar)
4. Click **Actions**

#### 8.2 Add BOT_TOKEN Secret

1. Click **New repository secret** (green button)
2. **Name:** `BOT_TOKEN`
3. **Secret:** `8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0`
4. Click **Add secret**

#### 8.3 Add CHAT_ID Secret

1. Click **New repository secret** (green button)
2. **Name:** `CHAT_ID`
3. **Secret:** `-1003877235401`
4. Click **Add secret**

#### 8.4 Verify

You should see:
```
BOT_TOKEN  •••••••••
CHAT_ID    •••••••••
```

---

### **STEP 9: Test the Workflow**

#### 9.1 Go to Actions Tab

1. Open your repo: https://github.com/pav715/degree-jobs-fresher-bot
2. Click **Actions** (top menu)

#### 9.2 Click Your Workflow

1. Left sidebar: Click **Degree Jobs Fresher Bot**

#### 9.3 Run Manually

1. Click **Run workflow** (top right, blue button)
2. Click **Run workflow** (in dropdown)
3. Wait 30 seconds

#### 9.4 Check Execution

1. Refresh the page
2. You'll see a new run appear
3. Click on it to see steps executing:
   - ✅ Checkout code
   - ✅ Set up Python
   - ✅ Install dependencies
   - ✅ Run bot
   - ✅ Commit updates

**If all steps are green ✅:** SUCCESS!

#### 9.5 Check Telegram

1. Open Telegram
2. Go to **Degree Jobs Fresher-Hyd** channel
3. If jobs were found, they should appear!

---

## 🔄 Automation Enabled

After step 9, your bot will:
- ✅ Run every 10 minutes automatically
- ✅ Check for fresher jobs
- ✅ Post to Telegram
- ✅ No local PC needed
- ✅ 24/7 running

---

## 📋 Summary

| Step | What | Status |
| :--- | :--- | :--- |
| 1-6 | Push code to GitHub | ✅ DONE |
| 7 | Create workflow file | → DO THIS |
| 8 | Add secrets | → THEN THIS |
| 9 | Test workflow | → FINALLY THIS |
| 10 | Monitor Telegram | ✅ DONE AUTOMATICALLY |

---

## ✨ Quick Checklist

### Step 7: Workflow File
- [ ] Create `.github/workflows/bot.yml`
- [ ] Paste YAML content
- [ ] Run: `git add .github/workflows/bot.yml`
- [ ] Run: `git commit -m "Add GitHub Actions workflow"`
- [ ] Run: `git push`

### Step 8: GitHub Secrets
- [ ] Go to repo Settings → Secrets and variables → Actions
- [ ] Add `BOT_TOKEN`: `8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0`
- [ ] Add `CHAT_ID`: `-1003877235401`
- [ ] Verify both are listed

### Step 9: Test
- [ ] Go to Actions tab
- [ ] Click "Degree Jobs Fresher Bot"
- [ ] Click "Run workflow"
- [ ] Watch steps execute (all green ✅)
- [ ] Check Telegram for jobs

---

## 🎉 After These Steps

Your bot will be **fully automated** and running 24/7 on GitHub!

---

**Ready? Start with Step 7!** 🚀
