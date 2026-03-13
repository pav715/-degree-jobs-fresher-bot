# Your Exact GitHub Commands

## Your Details:
- **GitHub Username:** pav715
- **Repository URL:** https://github.com/pav715/degree-jobs-fresher-bot.git
- **Bot Folder:** C:\1 API's work\Test 24\Degree Jobs Fresher

---

# COPY & PASTE THESE COMMANDS

## Command 1: Navigate to Bot Folder
```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
```
**What it does:** Goes to your bot folder

---

## Command 2: Initialize Git
```bash
git init
```
**What it does:** Creates a git repository in your folder

---

## Command 3: Add All Files
```bash
git add .
```
**What it does:** Stages all your bot files for upload

---

## Command 4: Create First Commit
```bash
git commit -m "Initial commit: Degree Jobs Fresher Bot - TAX focus + All fresher jobs"
```
**What it does:** Creates a snapshot of your code

---

## Command 5: Add GitHub Remote
```bash
git remote add origin https://github.com/pav715/degree-jobs-fresher-bot.git
```
**What it does:** Connects your local folder to GitHub repository

---

## Command 6: Rename Branch to Main
```bash
git branch -M main
```
**What it does:** Renames your branch to "main"

---

## Command 7: Push to GitHub
```bash
git push -u origin main
```
**What it does:** Uploads your code to GitHub

**⚠️ When asked for password:**
- **Username:** pav715
- **Password:** Use your Personal Access Token (get from Step 8 below if you don't have one)

---

## Getting Personal Access Token (if needed)

If `git push` asks for password and you don't have a token:

1. Go to: https://github.com/settings/tokens
2. Click **Generate new token (classic)**
3. Fill:
   - **Token name:** `bot-token`
   - **Expiration:** 90 days
   - **Scopes:** Check `repo` and `workflow`
4. Click **Generate token**
5. **COPY the token immediately** (you won't see it again!)
6. Paste this token as your password when git asks

---

# ✅ QUICK EXECUTION GUIDE

### Open Command Prompt and Run These (One by One):

**1. Navigate to folder:**
```bash
cd "C:\1 API's work\Test 24\Degree Jobs Fresher"
```

**2. Initialize:**
```bash
git init
```

**3. Add all files:**
```bash
git add .
```

**4. Commit:**
```bash
git commit -m "Initial commit: Degree Jobs Fresher Bot - TAX focus + All fresher jobs"
```

**5. Add remote:**
```bash
git remote add origin https://github.com/pav715/degree-jobs-fresher-bot.git
```

**6. Rename branch:**
```bash
git branch -M main
```

**7. Push (this will ask for password/token):**
```bash
git push -u origin main
```

---

## Expected Outputs

### After Command 2 (git init):
```
Initialized empty Git repository in C:\1 API's work\Test 24\Degree Jobs Fresher\.git
```

### After Command 4 (git commit):
```
[main (root-commit) abc1234] Initial commit: Degree Jobs Fresher Bot
 15 files changed, 500 insertions(+)
```

### After Command 7 (git push):
```
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Writing objects: 100% (15/15), 5.00 KiB | 5.00 KiB/s, done.
Total 15 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/pav715/degree-jobs-fresher-bot.git
 * [new branch]      main -> main
Branch 'main' set to track remote branch 'main' from 'origin'.
```

✅ **If you see this, your code is on GitHub!**

---

## Next Steps After Pushing Code

1. ✅ Code pushed to GitHub
2. → Create workflow file (.github/workflows/bot.yml)
3. → Add secrets (BOT_TOKEN, CHAT_ID)
4. → Test workflow
5. → Monitor Telegram for jobs

See: **GITHUB_CHECKLIST.md** (Step 7 onwards)

---

## Need Help?

**Error:** "fatal: not a git repository"
- **Solution:** Make sure you ran `git init` first

**Error:** "Permission denied"
- **Solution:** Use Personal Access Token (not GitHub password)

**Error:** "git not found"
- **Solution:** Download Git from https://git-scm.com/

---

**Ready? Open Command Prompt and start running commands!** 🚀
