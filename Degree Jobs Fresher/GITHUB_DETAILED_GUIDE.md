# GitHub Setup - Complete Detailed Guide with Screenshots

## 📱 Overview
You'll do these 12 steps to push your bot to GitHub and make it run 24/7:

```
Step 1: Create GitHub Account
    ↓
Step 2: Create Repository
    ↓
Step 3-6: Push Your Code
    ↓
Step 7-8: Add Workflow (Automation)
    ↓
Step 9: Add Secrets (Bot Token & Chat ID)
    ↓
Step 10: Test
    ↓
Step 11-12: Monitor
```

---

# PART 1: SETUP (Steps 1-3)

## STEP 1: Create GitHub Account

### 1.1 Open Browser
Go to: **https://github.com**

You'll see this page:
```
┌─────────────────────────────────────┐
│    GitHub - Where the world        │
│    builds software                  │
│                                     │
│  Email address:  [____________]     │
│  Password:       [____________]     │
│  Username:       [____________]     │
│                                     │
│  [Sign up for GitHub]               │
└─────────────────────────────────────┘
```

### 1.2 Fill the Form
- **Email:** Your email address
- **Password:** Create a strong password (mix of uppercase, lowercase, numbers)
- **Username:** `your-name` (this will be in your GitHub URL)

### 1.3 Click "Sign up for GitHub"

### 1.4 Verify Email
- GitHub sends you an email
- Click the link in the email
- Your account is ready! ✅

---

## STEP 2: Create Repository

### 2.1 After Login, Look for **+** Icon
Top right corner of GitHub page:
```
┌─────────────────────────────┐
│  Profile  ▼  +  🔔  👤     │
└─────────────────────────────┘
```

Click the **+** icon

### 2.2 Click "New repository"
```
+ New repository
+ New gist
+ New organization
+ Import repository
```

### 2.3 Fill Repository Form
You'll see a form. Fill it:

**Repository name:**
```
degree-jobs-fresher-bot
```

**Description (optional):**
```
Telegram bot for fresher jobs in Hyderabad & Telangana
```

**Visibility:**
- Select **Public** (green button)

**Scroll down and click:**
```
[Create repository]
```

### 2.4 You'll See Success Page
Shows:
```
Quick setup — if you've done this kind of thing before
or:
https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git
```

**👉 COPY THIS URL!** You'll need it.

---

## STEP 3: Prepare Local Machine

### 3.1 Check If Git is Installed
Open **Command Prompt** (Windows):
- Press: **Windows Key + R**
- Type: `cmd`
- Press Enter

Type this command:
```bash
git --version
```

If you see something like `git version 2.40.0`, Git is installed ✅

If you get "command not found", download Git from: https://git-scm.com/

### 3.2 Navigate to Your Bot Folder
In Command Prompt, type:
```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
```

Press Enter

You should see:
```
C:\1 API's work\Test 24\Degree Jobs Fresher>
```

### 3.3 Check Your Files
Type:
```bash
ls -la
```

You should see these files:
```
bot.py
config.py
scraper.py
sender.py
requirements.txt
README.md
bot.log
seen_jobs.json
```

If you see them, you're ready! ✅

---

# PART 2: PUSH YOUR CODE (Steps 4-6)

## STEP 4: Initialize Git

### 4.1 Initialize Repository
In Command Prompt (in your bot folder), type:
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

(This stages all your files for upload. No output = success)

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

## STEP 5: Connect to GitHub

### 5.1 Add Remote Connection
Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git
```

**Example:**
```bash
git remote add origin https://github.com/john-smith/degree-jobs-fresher-bot.git
```

(No output = success)

### 5.2 Verify Connection
```bash
git remote -v
```

Should show:
```
origin  https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git (fetch)
origin  https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git (push)
```

### 5.3 Rename Branch
```bash
git branch -M main
```

(No output = success)

---

## STEP 6: Push to GitHub

### 6.1 First Time Push
```bash
git push -u origin main
```

### 6.2 Get Personal Access Token (if needed)
If you get a browser popup, you might need a Personal Access Token.

**Get token:**
1. Go to: https://github.com/settings/tokens
2. Click **Generate new token (classic)**
3. Fill:
   - **Token name:** `bot-token`
   - **Expiration:** 90 days
   - **Scopes:** Check `repo` and `workflow`
4. Click **Generate token**
5. **COPY the token** (you won't see it again!)

### 6.3 Enter Token as Password
When git asks:
```
Username for 'https://github.com': YOUR_USERNAME
Password for 'https://...': [PASTE YOUR TOKEN HERE]
```

Paste your token and press Enter.

### 6.4 Success!
You'll see:
```
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Writing objects: 100% (9/9), 2.50 KiB | 2.50 MiB/s, done.
Total 9 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git
 * [new branch]      main -> main
Branch 'main' set to track remote branch 'main' from 'origin'.
```

✅ **Your code is now on GitHub!**

---

# PART 3: AUTOMATION (Steps 7-9)

## STEP 7: Create Workflow File

### 7.1 Create Folders
In Command Prompt, in your bot folder, type:
```bash
mkdir -p .github/workflows
```

(No output = success)

This creates:
```
.github/
└── workflows/
```

### 7.2 Create File `.github/workflows/bot.yml`

Open a text editor (**Notepad** or **VS Code**):
- Right-click in your bot folder
- Choose **New** → **Text Document**
- Name it: `bot.yml`
- Move it to `.github/workflows/` folder

**OR use Command Prompt to create it:**
```bash
echo > .github/workflows/bot.yml
```

Then edit it (open with Notepad).

### 7.3 Paste This Content

Copy and paste this entire content into `bot.yml`:

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

**Save the file!**

### 7.4 Your Folder Structure Now Looks Like
```
Degree Jobs Fresher/
├── .github/
│   └── workflows/
│       └── bot.yml              ← NEW FILE
├── bot.py
├── config.py
├── scraper.py
├── sender.py
├── requirements.txt
├── README.md
├── bot.log
├── seen_jobs.json
└── GITHUB_STEP_BY_STEP.md
```

---

## STEP 8: Push Workflow to GitHub

### 8.1 Add Workflow File
```bash
git add .github/workflows/bot.yml
```

### 8.2 Commit
```bash
git commit -m "Add GitHub Actions workflow"
```

### 8.3 Push
```bash
git push
```

Output:
```
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 342 bytes | 342.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
To https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git
   abc1234..def5678  main -> main
```

✅ **Workflow is on GitHub!**

---

## STEP 9: Add GitHub Secrets

**This is IMPORTANT!** The bot needs to know:
- Your Telegram BOT_TOKEN
- Your Telegram CHAT_ID

### 9.1 Go to Repository Settings
1. Open your GitHub repo:
   ```
   https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot
   ```

2. Click **Settings** (top menu bar)

3. Click **Secrets and variables** (left sidebar)

4. Click **Actions**

### 9.2 Add BOT_TOKEN Secret

Click: **New repository secret** (green button)

Fill:
- **Name:** `BOT_TOKEN`
- **Secret:** `8534310272:AAEJKeBKc7t92nb5xd_XNNVWrYIeOvqlIH0`

Click: **Add secret**

✅ You'll see it added (as dots: `•••••`)

### 9.3 Add CHAT_ID Secret

Click: **New repository secret** (green button again)

Fill:
- **Name:** `CHAT_ID`
- **Secret:** `-1003877235401`

Click: **Add secret**

✅ You'll see it added (as dots: `•••••`)

### 9.4 Verify Both Are There
You should now see in Secrets section:
```
BOT_TOKEN  •••••••••
CHAT_ID    •••••••••
```

---

# PART 4: TEST & MONITOR (Steps 10-12)

## STEP 10: Test the Workflow

### 10.1 Go to Actions Tab
1. Open your repo on GitHub
2. Click **Actions** (top menu bar)

You'll see:
```
All workflows
Degree Jobs Fresher Bot  ← Click this
```

### 10.2 Click Your Workflow
Click: **Degree Jobs Fresher Bot**

### 10.3 Run Manually
Click: **Run workflow** (top right, blue button)

A dropdown appears:
```
Use workflow from
  Branch: main
  [Run workflow]
```

Click: **Run workflow**

### 10.4 Watch It Run
You'll see a new run appear. Click it to see details:

```
Degree Jobs Fresher Bot #1
- Checkout code                    ✅
- Set up Python                    ✅
- Install dependencies             ✅
- Run bot                          ✅
- Commit updates                   ✅
```

If you see green ✅ on all steps: **SUCCESS!**

### 10.5 Check Your Telegram Channel
- Open **Degree Jobs Fresher-Hyd** channel
- You might see new jobs posted!

---

## STEP 11: Automatic Scheduling

**Now the bot runs automatically!**

### 11.1 How It Works
- GitHub runs the workflow **every 10 minutes**
- Your PC doesn't need to be on
- Bot keeps searching for jobs
- Posts to Telegram automatically

### 11.2 View All Runs
1. Go to your repo → **Actions** tab
2. Click **Degree Jobs Fresher Bot**
3. You'll see list of runs:
   ```
   - Workflow run #5  ✅  10 mins ago
   - Workflow run #4  ✅  20 mins ago
   - Workflow run #3  ✅  30 mins ago
   ```

Click any run to see what happened.

### 11.3 Check Logs
Click any run and scroll down to see:
- What jobs were found
- What was posted to Telegram
- Any errors (if any)

---

## STEP 12: Monitor Telegram Channel

### 12.1 Open Telegram
- App or Web: https://web.telegram.org
- Go to: **Degree Jobs Fresher-Hyd** channel

### 12.2 You'll See Jobs Like:
```
📌 Tax Assistant (Fresher)
Company: ABC Inc
Location: Hyderabad
Source: LinkedIn

🔗 Apply Now

---

📌 Accounts Executive
Company: XYZ Bank
Location: Telangana
Source: Naukri

🔗 Apply Now
```

---

# ✅ SUMMARY

You've successfully:

| Step | Action | Status |
| :--- | :--- | :--- |
| 1 | Created GitHub account | ✅ |
| 2 | Created repository | ✅ |
| 3 | Prepared local code | ✅ |
| 4 | Initialized Git | ✅ |
| 5 | Connected to GitHub | ✅ |
| 6 | Pushed code | ✅ |
| 7 | Created workflow file | ✅ |
| 8 | Pushed workflow | ✅ |
| 9 | Added secrets | ✅ |
| 10 | Tested manually | ✅ |
| 11 | Automation enabled | ✅ |
| 12 | Monitor channel | ✅ |

---

# 🎉 RESULT

Your bot now:
- ✅ Runs 24/7 on GitHub servers
- ✅ Checks for jobs every 10 minutes
- ✅ Posts to Telegram automatically
- ✅ No local machine needed
- ✅ FREE (GitHub free tier)
- ✅ Tracked on GitHub (version control)

---

# 📝 Future Updates

If you want to change keywords or config:

1. Edit `config.py` locally
2. Run:
   ```bash
   git add .
   git commit -m "Updated keywords"
   git push
   ```
3. Done! GitHub automatically uses new code next run

---

# 🆘 TROUBLESHOOTING

### "Bot won't start" error in GitHub
- Check **Actions** tab → click the red ❌ run
- See what error is shown
- Common: Missing secrets (check Step 9)

### "Jobs not posting to Telegram"
- Verify CHAT_ID is correct (Step 9.3)
- Verify bot is admin in Telegram channel
- Check workflow logs for errors

### "git push asks for password"
- Use Personal Access Token (Step 6.2)
- Never use your GitHub password

### "Can't find .github folder"
- Make sure you ran: `mkdir -p .github/workflows`
- File path is exactly: `.github/workflows/bot.yml`

---

**✨ You're all set! Your bot is now live on GitHub!** 🚀
