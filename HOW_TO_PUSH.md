# 🚀 How to Push Files to GitHub

**Problem:** Web upload didn't properly add requirements.txt to GitHub. Your local files are ready but not pushed.

**Solution:** Run the push script to force-push your local files to GitHub.

---

## Option 1: PowerShell Script (Recommended)

### Step 1: Open PowerShell
1. Press `Win + X`
2. Click "Windows PowerShell (Admin)" or "Terminal (Admin)"

### Step 2: Run the Script
```powershell
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
powershell -ExecutionPolicy Bypass -File PUSH_TO_GITHUB.ps1
```

### Step 3: Enter GitHub Credentials
- **Username:** `pav715`
- **Password:** Use your Personal Access Token (see below)

### Step 4: Wait for Success ✅

---

## Option 2: Batch Script (Alternative)

### Step 1: Open Command Prompt
1. Press `Win + R`
2. Type `cmd` and press Enter

### Step 2: Run the Script
```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
PUSH_TO_GITHUB.bat
```

### Step 3: Enter GitHub Credentials
- **Username:** `pav715`
- **Password:** Use your Personal Access Token

### Step 4: Wait for Success ✅

---

## Getting Your Personal Access Token

**If you don't have a token yet:**

### Step 1: Go to GitHub Settings
1. Go to: https://github.com/settings/tokens
2. Sign in if needed

### Step 2: Generate New Token
1. Click **"Generate new token (classic)"** button
2. Fill in:
   - **Token name:** `bot-token`
   - **Expiration:** `90 days`
   - **Scopes:** Check ✓ `repo` and ✓ `workflow`
3. Click **"Generate token"**

### Step 3: Copy Your Token
- **IMPORTANT:** Copy the token immediately (you won't see it again!)
- Save it somewhere safe (Notepad, password manager, etc.)

### Step 4: Use Token as Password
When the script asks for password, paste your token.

---

## What the Script Does

1. ✅ Verifies all 5 critical files exist locally
2. ✅ Shows what will be pushed to GitHub
3. ✅ Asks for confirmation
4. ✅ Pushes files to GitHub with `git push --force`
5. ✅ Verifies the push was successful

---

## After Push - Next Steps

Once the script shows "SUCCESS!", do this:

### Step 1: Verify on GitHub
1. Go to: https://github.com/pav715/degree-jobs-fresher-bot
2. Refresh the page
3. You should see all files:
   - ✅ bot.py
   - ✅ config.py
   - ✅ sender.py
   - ✅ scraper.py
   - ✅ requirements.txt

### Step 2: Create Workflow File
1. On GitHub, click **"Add file"** → **"Create new file"**
2. File name: `.github/workflows/bot.yml`
3. Paste this content:

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

4. Click **"Commit changes"**

### Step 3: Add GitHub Secrets
1. Go to **Settings** (top menu)
2. Click **"Secrets and variables"** → **"Actions"** (left sidebar)
3. Click **"New repository secret"** (green button)
4. Add two secrets:

**Secret 1: BOT_TOKEN**
- Name: `BOT_TOKEN`
- Value: `8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0`
- Click **"Add secret"**

**Secret 2: CHAT_ID**
- Name: `CHAT_ID`
- Value: `-1003877235401`
- Click **"Add secret"**

### Step 4: Test the Workflow
1. Go to **Actions** tab (top menu)
2. Click **"Degree Jobs Fresher Bot"** (left sidebar)
3. Click **"Run workflow"** (blue button, top right)
4. Click **"Run workflow"** (in dropdown)
5. Wait 30 seconds and refresh
6. Click on the run to see steps executing
7. Check Telegram for jobs!

---

## ❓ Troubleshooting

### "Authentication failed" / "Permission denied"
- Make sure you're using a **Personal Access Token**, not your GitHub password
- Token should have `repo` and `workflow` scopes
- Token should not be expired (90 days)

### "Fatal: not a git repository"
- Make sure you're in the correct directory:
  ```
  cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
  ```

### "Requirements.txt not found" on GitHub Actions
- This means the push didn't work
- Run the script again with proper authentication

### Push still failing?
- Try running the PowerShell script with admin rights
- Close other Git/GitHub applications
- Restart your computer

---

## ✅ Complete Checklist

- [ ] Run PUSH_TO_GITHUB.ps1 or PUSH_TO_GITHUB.bat
- [ ] Enter GitHub credentials (username + token)
- [ ] See "SUCCESS!" message
- [ ] Go to GitHub repo and verify files are there
- [ ] Create `.github/workflows/bot.yml`
- [ ] Add BOT_TOKEN secret
- [ ] Add CHAT_ID secret
- [ ] Run workflow manually
- [ ] Check Telegram for jobs

---

**Ready? Run the script now!** 🚀
