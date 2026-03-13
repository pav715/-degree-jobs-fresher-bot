@echo off
REM This script pushes the bot files to GitHub
REM Requirements: Git installed, GitHub Personal Access Token

setlocal enabledelayedexpansion

echo ====================================
echo Degree Jobs Fresher Bot - GitHub Push
echo ====================================
echo.

cd /d "C:\1 API's work\Test 24\Degree Jobs Fresher"

if errorlevel 1 (
    echo ERROR: Could not change to directory
    pause
    exit /b 1
)

echo Current directory: %cd%
echo.

REM Check git status
echo Checking git status...
git status
echo.

REM Show what will be pushed
echo Files that will be pushed:
git diff --name-only origin/main HEAD 2>nul || echo (New commit, all files will be included)
echo.

REM Try to push
echo Pushing to GitHub...
echo Please enter your GitHub credentials when prompted.
echo.

git push -u origin main --force

if errorlevel 1 (
    echo.
    echo ERROR: Push failed!
    echo.
    echo If you see an authentication error:
    echo 1. Go to https://github.com/settings/tokens
    echo 2. Generate new token (classic)
    echo 3. Name: bot-token
    echo 4. Scopes: repo, workflow
    echo 5. Copy the token
    echo 6. Paste token as password when git asks
    echo.
    pause
    exit /b 1
)

echo.
echo SUCCESS! Files pushed to GitHub!
echo.
echo Next steps:
echo 1. Go to https://github.com/pav715/degree-jobs-fresher-bot
echo 2. Create .github/workflows/bot.yml (see NEXT_GITHUB_STEPS.md)
echo 3. Add GitHub Secrets (BOT_TOKEN and CHAT_ID)
echo 4. Run workflow manually to test
echo.

pause
