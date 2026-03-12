# GitHub Setup - Summary Card

## What is GitHub?
- Cloud storage for code
- Version control (track changes)
- GitHub Actions (free automation)
- Your bot runs 24/7 on their servers

---

## Why Use GitHub?
✅ Bot runs even when your PC is OFF
✅ Automatic updates every 10 minutes
✅ Free (GitHub free tier)
✅ Professional workflow
✅ Easy to manage & update

---

## 12-Step GitHub Setup

### Phase 1: Preparation (Steps 1-3)
1. Create GitHub account (free at github.com)
2. Create repository named `degree-jobs-fresher-bot`
3. Prepare your bot code locally

### Phase 2: Push Code (Steps 4-6)
4. Initialize Git in your bot folder
5. Commit your code
6. Connect to GitHub & push

### Phase 3: Setup Automation (Steps 7-9)
7. Create `.github/workflows/bot.yml` file
8. Push workflow to GitHub
9. Add secrets (BOT_TOKEN, CHAT_ID)

### Phase 4: Testing & Activation (Steps 10-12)
10. Test manually via GitHub Actions
11. Automation starts (every 10 minutes)
12. Monitor Telegram channel

---

## Total Time: ~30 minutes

- GitHub account: 2 min
- Create repo: 1 min
- Push code: 5 min
- Create workflow: 10 min
- Add secrets: 5 min
- Test: 3 min

**Done!** ✅ Bot now runs 24/7 on GitHub

---

## Files You'll Create

```
.github/workflows/bot.yml     ← ONE new file to create
```

Everything else is just pushing existing code to GitHub.

---

## Copy-Paste Ready

See **GITHUB_QUICK_REFERENCE.md** for all commands you need.

Just copy → paste → replace YOUR_USERNAME → done!

---

## What Happens After Setup

### Every 10 Minutes:
1. GitHub runs your bot.py
2. Bot searches for fresher jobs
3. Posts to Telegram channel
4. Updates bot.log & seen_jobs.json
5. Repeats...

### Your PC:
- Can be OFF ✅
- No setup needed
- No downloads needed
- Works automatically

---

## Key Files

| File | Purpose |
| :--- | :--- |
| `GITHUB_STEP_BY_STEP.md` | Full detailed guide (read first) |
| `GITHUB_QUICK_REFERENCE.md` | All commands to copy-paste |
| `GITHUB_SETUP.md` | Original detailed guide |
| `.github/workflows/bot.yml` | Automation config (create this) |

---

## When Things Go Wrong

**Workflow won't run?**
- Check Actions tab for red ❌ errors
- Verify secrets are correct
- Check bot.log for details

**Jobs not posting?**
- Verify CHAT_ID is correct
- Ensure bot is admin in Telegram
- Check workflow logs

**Push fails?**
- Use Personal Access Token (not password)
- Get token from: github.com/settings/tokens
- Give `repo` and `workflow` permissions

---

## Next Steps After GitHub Setup

1. ✅ Bot runs 24/7 on GitHub
2. ⏭️ Create B.Tech Fresher Bot (copy same process)
3. ⏭️ Create M.Tech Fresher Bot (copy same process)
4. ⏭️ Monitor all 3 channels for jobs

---

## One Command to Remember

After any code change:
```bash
git add . && git commit -m "description" && git push
```

Done! GitHub uses your new code automatically.

---

## Resources

- GitHub: https://github.com
- Git Documentation: https://git-scm.com/doc
- GitHub Actions: https://github.com/features/actions
- Personal Access Token: https://github.com/settings/tokens

---

## Ready?

1. Read: **GITHUB_STEP_BY_STEP.md** (detailed version)
2. Reference: **GITHUB_QUICK_REFERENCE.md** (copy-paste)
3. Execute: Follow the 12 steps
4. Test: Run workflow manually
5. Monitor: Check Telegram channel

**Total time: ~30 minutes**

🚀 **You got this!**

---

## Support

If stuck on any step, re-read that step in GITHUB_STEP_BY_STEP.md

It's designed to be exactly followed step-by-step.

No advanced knowledge needed - just copy-paste commands!

✅ **Let's go!**
