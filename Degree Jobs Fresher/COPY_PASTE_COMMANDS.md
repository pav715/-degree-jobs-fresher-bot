# GitHub Setup - Copy & Paste Commands Only

**Just copy each command and paste into Command Prompt. That's it!**

---

## Commands for STEP 4-6: Push Code to GitHub

### Command 1: Navigate to Bot Folder
```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
```
Paste and press Enter.

---

### Command 2: Initialize Git
```bash
git init
```
Paste and press Enter.

---

### Command 3: Add All Files
```bash
git add .
```
Paste and press Enter.

---

### Command 4: Create First Commit
```bash
git commit -m "Initial commit: Degree Jobs Fresher Bot"
```
Paste and press Enter.

---

### Command 5: Add Remote to GitHub
⚠️ **REPLACE `YOUR_USERNAME` with your GitHub username first!**

Example: If your username is `john-smith`, use:
```bash
git remote add origin https://github.com/john-smith/degree-jobs-fresher-bot.git
```

**Copy the command with YOUR username and paste.**

---

### Command 6: Rename Branch
```bash
git branch -M main
```
Paste and press Enter.

---

### Command 7: Push to GitHub
```bash
git push -u origin main
```
Paste and press Enter.

**When asked for password, paste your Personal Access Token (from Step 6.2 in detailed guide).**

---

## Commands for STEP 7-8: Add Workflow

### Command 8: Create Workflow Folder
```bash
mkdir -p .github/workflows
```
Paste and press Enter.

---

### Command 9: Add Workflow File
```bash
git add .github/workflows/bot.yml
```
Paste and press Enter.

---

### Command 10: Commit Workflow
```bash
git commit -m "Add GitHub Actions workflow"
```
Paste and press Enter.

---

### Command 11: Push Workflow
```bash
git push
```
Paste and press Enter.

---

## All 11 Commands Summary

If you want to do everything at once, just copy each line (one at a time):

```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
git init
git add .
git commit -m "Initial commit: Degree Jobs Fresher Bot"
git remote add origin https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git
git branch -M main
git push -u origin main
mkdir -p .github/workflows
git add .github/workflows/bot.yml
git commit -m "Add GitHub Actions workflow"
git push
```

---

## Important Notes

1. **Replace `YOUR_USERNAME`** with your actual GitHub username
   - Example: `john-smith`, `alice123`, etc.

2. **For `git push`, you need a Personal Access Token**
   - Get it from: https://github.com/settings/tokens
   - Use token as password (not your GitHub password)

3. **Create `.github/workflows/bot.yml` file with content from STEP 7**
   - Use Notepad or VS Code to create it
   - Paste the YAML content from GITHUB_DETAILED_GUIDE.md (STEP 7.3)

4. **After Steps 1-11, you need to add Secrets in GitHub web interface (STEP 9)**
   - Can't be done with commands
   - Must be done manually on GitHub website

---

## Expected Output After Each Command

### git init
```
Initialized empty Git repository in C:\1 API's work\Test 24\Degree Jobs Fresher\.git
```

### git add .
(No output = success)

### git commit -m "Initial..."
```
[main (root-commit) abc1234] Initial commit: Degree Jobs Fresher Bot
 9 files changed, 500 insertions(+)
```

### git remote add origin
(No output = success)

### git branch -M main
(No output = success)

### git push -u origin main
```
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Writing objects: 100% (9/9), 2.50 KiB | 2.50 MiB/s, done.
Total 9 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git
 * [new branch]      main -> main
Branch 'main' set to track remote branch 'main' from 'origin'.
```

### mkdir -p .github/workflows
(No output = success)

### git add .github/workflows/bot.yml
(No output = success)

### git commit -m "Add GitHub..."
```
[main abc1234..def5678] Add GitHub Actions workflow
 1 file changed, 20 insertions(+)
```

### git push
```
Enumerating objects: 3, done.
To https://github.com/YOUR_USERNAME/degree-jobs-fresher-bot.git
   abc1234..def5678  main -> main
```

---

## Checklist Before You Start

- [ ] GitHub account created
- [ ] Repository created on GitHub
- [ ] Git installed on your PC (`git --version` shows version)
- [ ] You're in correct folder (`C:\1 API's work\Test 24\Degree Jobs Fresher`)
- [ ] You have Personal Access Token ready (from Step 6.2)
- [ ] `.github/workflows/bot.yml` file created with YAML content

---

## Then After Commands:

- [ ] Go to GitHub website
- [ ] Add BOT_TOKEN secret (Step 9.2)
- [ ] Add CHAT_ID secret (Step 9.3)
- [ ] Go to Actions → Run workflow manually (Step 10)
- [ ] Check Telegram for jobs (Step 12)

---

**That's it! Your bot will run 24/7 on GitHub!** 🚀
