# PowerShell script to push files to GitHub
# Run as: powershell -ExecutionPolicy Bypass -File PUSH_TO_GITHUB.ps1

Write-Host "====================================" -ForegroundColor Cyan
Write-Host "Degree Jobs Fresher Bot - GitHub Push" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""

$botDir = "C:\1 API's work\Test 24\Degree Jobs Fresher"

# Check if directory exists
if (-not (Test-Path $botDir)) {
    Write-Host "ERROR: Directory not found: $botDir" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Set-Location $botDir
Write-Host "Current directory: $(Get-Location)" -ForegroundColor Green
Write-Host ""

# Check git status
Write-Host "Checking git status..." -ForegroundColor Yellow
git status
Write-Host ""

# List files to be pushed
Write-Host "Files in repository:" -ForegroundColor Yellow
git ls-files | Sort-Object
Write-Host ""

# Verify critical files exist
Write-Host "Verifying critical files..." -ForegroundColor Yellow
$criticalFiles = @("bot.py", "config.py", "sender.py", "scraper.py", "requirements.txt")
$allExist = $true

foreach ($file in $criticalFiles) {
    if (Test-Path $file) {
        $size = (Get-Item $file).Length
        Write-Host "  ✓ $file ($size bytes)" -ForegroundColor Green
    } else {
        Write-Host "  ✗ MISSING: $file" -ForegroundColor Red
        $allExist = $false
    }
}

Write-Host ""

if (-not $allExist) {
    Write-Host "ERROR: Some critical files are missing!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Ask for confirmation
Write-Host "Ready to push to GitHub?" -ForegroundColor Cyan
Write-Host "This will force-push the local commit and overwrite GitHub." -ForegroundColor Yellow
$confirm = Read-Host "Continue? (yes/no)"

if ($confirm -ne "yes") {
    Write-Host "Cancelled." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "Please enter your GitHub credentials when prompted." -ForegroundColor Gray
Write-Host ""

# Attempt push
$output = git push -u origin main --force 2>&1
$exitCode = $LASTEXITCODE

Write-Host $output
Write-Host ""

if ($exitCode -eq 0) {
    Write-Host "SUCCESS! Files pushed to GitHub!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Cyan
    Write-Host "1. Go to https://github.com/pav715/degree-jobs-fresher-bot" -ForegroundColor White
    Write-Host "2. Create .github/workflows/bot.yml (see NEXT_GITHUB_STEPS.md)" -ForegroundColor White
    Write-Host "3. Add GitHub Secrets (BOT_TOKEN and CHAT_ID)" -ForegroundColor White
    Write-Host "4. Run workflow manually to test" -ForegroundColor White
    Write-Host ""

    # Verify push
    Write-Host "Verifying push..." -ForegroundColor Yellow
    git log --oneline -1
    git remote -v
} else {
    Write-Host "ERROR: Push failed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "If you see authentication error:" -ForegroundColor Yellow
    Write-Host "1. Go to https://github.com/settings/tokens" -ForegroundColor Gray
    Write-Host "2. Generate new token (classic)" -ForegroundColor Gray
    Write-Host "3. Name: bot-token" -ForegroundColor Gray
    Write-Host "4. Scopes: repo, workflow" -ForegroundColor Gray
    Write-Host "5. Copy the token" -ForegroundColor Gray
    Write-Host "6. Paste token as password when git asks" -ForegroundColor Gray
}

Write-Host ""
Read-Host "Press Enter to exit"
