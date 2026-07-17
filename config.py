import os

# ── Telegram ─────────────────────────────────────────────────────────
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHAT_ID   = os.environ.get("CHAT_ID", "")

# ── Search keywords (any-degree fresher roles) ───────────────────────
# NOTE: total scrape combinations = len(KEYWORDS) x len(LOCATIONS).
# Keep the product under ~120 so the GitHub Actions run finishes in time.
# Current: 17 keywords x 7 locations = 119 combinations.
KEYWORDS = [
    # Generic any-degree fresher
    "Fresher",
    "Any Graduate",
    "Entry Level",
    "Graduate Trainee",
    "Management Trainee",
    # High-volume any-degree roles
    "Data Entry",
    "Back Office Executive",
    "Customer Support Fresher",
    "BPO Fresher",
    "Voice Process",
    "Non Voice Process",
    "Operations Executive",
    # Functional fresher roles
    "HR Executive Fresher",
    "Sales Executive Fresher",
    # Tax / accounting-adjacent entry roles
    "Tax Assistant",
    "Accounting Fresher",
    "Audit Assistant",
]

# ── Locations (South India + Remote) ─────────────────────────────────
# 7 search locations to stay under the combination budget.
# The scraper's location filter additionally accepts Telangana,
# Thiruvananthapuram, Vijayawada, and India-wide/remote postings.
LOCATIONS = [
    "Hyderabad",
    "Bangalore",
    "Chennai",
    "Coimbatore",
    "Kochi",
    "Visakhapatnam",
    "Remote",
]

# ── Timing ────────────────────────────────────────────────────────────
CHECK_INTERVAL_MINUTES = 10   # Check every 10 minutes
