import os

# ── Telegram ─────────────────────────────────────────────────────────
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHAT_ID   = os.environ.get("CHAT_ID", "")

# ── PRIMARY FOCUS: TAX + All Fresher Jobs ──────────────────────────
# Search for ANY fresher jobs + TAX jobs (primary focus)
# No role filtering - all jobs posted

KEYWORDS = [
    # ── TAX (PRIMARY FOCUS) ──
    "Tax",
    "Income Tax",
    "Taxation",
    "Tax Compliance",
    "Tax Assistant",
    "Tax Analyst",
    "Tax Consultant",
    "Tax Advisor",
    "Tax Professional",
    "Tax Officer",
    "Tax Inspector",
    "Tax Processor",
    "Tax Accountant",
    "Direct Tax",
    "Indirect Tax",
    "GST",
    "TDS",
    "Income Tax Department",
    "Tax Deduction",
    "Tax Filing",
    "Tax Planning",
    "Tax Forms",
    "Tax Returns",
    "ITR",
    "Tax Computation",
    "Tax Preparation",
    "Tax Audit",
    "Tax Compliance Officer",
    "Regulatory Tax",

    # ── Fresher Keywords (BROAD) ──
    "Fresher",
    "Entry Level",
    "Graduate",
    "Graduate Jobs",
    "Fresher Jobs",
    "Recent Graduate",
    "New Graduate",
    "First Job",
    "Campus Hire",
    "Graduate Trainee",
    "0-1 years",
    "0 years experience",
    "Less than 1 year",

    # ── ALL Degree Types (No B.Tech/M.Tech) ──
    "Bachelor of Arts",
    "B.A",
    "Bachelor of Science",
    "B.Sc",
    "Bachelor of Commerce",
    "B.Com",
    "Bachelor of Business Administration",
    "BBA",
    "Bachelor of Computer Applications",
    "BCA",
    "Bachelor of Education",
    "B.Ed",
    "Bachelor of Social Work",
    "BSW",
    "Bachelor of Vocational",
    "B.Vocational",
    "Master of Science",
    "M.Sc",
    "Master of Commerce",
    "M.Com",
    "Master of Business Administration",
    "MBA",
    "Master of Computer Applications",
    "MCA",
    "Postgraduate",
    "PG Diploma",
    "Graduate Degree",
    "Any Graduate",
    "Any Degree",

    # ── ALL Job Categories (Broad Search) ──
    "Jobs",
    "Employment",
    "Vacancy",
    "Opening",
    "Recruitment",
    "Hiring",
    "Career",
    "Position",
    "Role",
    "Opportunity",

    # ── ALL Industries ──
    "Finance",
    "Banking",
    "Accounting",
    "Audit",
    "Insurance",
    "BPO",
    "IT",
    "Information Technology",
    "Software",
    "Consulting",
    "Healthcare",
    "Pharma",
    "Retail",
    "Manufacturing",
    "E-Commerce",
    "Logistics",
    "Education",
    "Media",
    "Government",
    "Public Sector",
    "Private Sector",
    "Startup",
    "Corporate",
    "Service",
    "FMCG",
    "Real Estate",

    # ── ALL Roles (Entry-Level) ──
    "Associate",
    "Trainee",
    "Coordinator",
    "Assistant",
    "Executive",
    "Officer",
    "Analyst",
    "Developer",
    "Engineer",
    "Consultant",
    "Specialist",
    "Representative",
    "Intern",
    "Apprentice",
    "Support",
    "Administrator",
    "Clerk",
    "Operator",
    "Technician",
    "Supervisor",
]

# ── Locations (Hyderabad & Telangana Only) ────────────────────────────
LOCATIONS = [
    "Hyderabad",
    "Hyderabad India",
    "Telangana",
    "Secunderabad",
    "Cyberabad",
]

# ── Timing ────────────────────────────────────────────────────────────
CHECK_INTERVAL_MINUTES = 10   # Check every 10 minutes

# ── Your Profile (used by AI for match scoring) ───────────────────────
USER_PROFILE = (
    "Looking for fresher positions in Hyderabad/Telangana. "
    "Interested in all degree programs: B.Tech, M.Tech, B.Sc, M.Sc, BCA, MCA, "
    "B.Com, MBA, Fine Arts, Design, and other UG/PG degrees. "
    "Entry-level roles preferred. Skills: Python, Java, Data Science, Web Development, "
    "Database Management, Cloud Computing. Location: Hyderabad, India."
)

# Only send jobs where AI match score >= this value (0 = send all)
MIN_MATCH_SCORE = 40

# Max jobs to send per cycle (prevents spam on first big batch)
MAX_JOBS_PER_CYCLE = 20

# ── Workday ATS Companies (verified URLs) ──────────────────────────────
WORKDAY_COMPANIES = [
    # ── IT / Tech Companies ──
    {"name": "Accenture",         "tenant": "accenture",       "path": "AccentureCareers",       "wd": 103},
    {"name": "Wipro",             "tenant": "wipro",           "path": "External",               "wd": 3},
    {"name": "Infosys",           "tenant": "infosys",         "path": "Infosys_Careers",        "wd": 1},
    {"name": "TCS",               "tenant": "tcs",             "path": "TCS_Careers",            "wd": 1},
    {"name": "Genpact",           "tenant": "genpact",         "path": "Genpact_Careers",        "wd": 1},
    {"name": "Cognizant",         "tenant": "cognizant",       "path": "CognizantCareers",       "wd": 1},
    {"name": "HCL Technologies",  "tenant": "hcl",             "path": "HCL_Careers",            "wd": 1},
    {"name": "Mphasis",           "tenant": "mphasis",         "path": "Mphasis_Careers",        "wd": 1},

    # ── Startups & Tech ──
    {"name": "Flipkart",          "tenant": "flipkart",        "path": "Flipkart_Careers",       "wd": 1},
    {"name": "Amazon",            "tenant": "amazon",          "path": "Amazon_Careers",         "wd": 1},
    {"name": "Google",            "tenant": "google",          "path": "Google_Careers",         "wd": 1},
    {"name": "Microsoft",         "tenant": "microsoft",       "path": "Microsoft_Careers",      "wd": 1},

    # ── Finance & Services ──
    {"name": "Fidelity",          "tenant": "fmr",             "path": "FidelityCareers",        "wd": 1},
    {"name": "Vanguard",          "tenant": "vanguard",        "path": "vanguard_external",      "wd": 5},
    {"name": "Deloitte",          "tenant": "deloitte",        "path": "Deloitte-Careers",       "wd": 1},
    {"name": "PwC",               "tenant": "pwc",             "path": "Global_Campus_Careers",  "wd": 3},
]

# ── India Job Portals (HTML scrape) ───────────────────────────────────
INDIA_PORTALS = [
    {"name": "Foundit",      "url": "https://www.foundit.in/srp/results?query=fresher&locations=Hyderabad&experience=0&freshness=1"},
    {"name": "Shine",        "url": "https://www.shine.com/job-search/fresher-jobs-in-hyderabad"},
    {"name": "TimesJobs",    "url": "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=fresher&sequence=2&startPage=1"},
    {"name": "Naukri",       "url": "https://www.naukri.com/fresher-jobs-hyderabad"},
]

# ── LinkedIn Job Search (Manual filter - scrape via search) ────────────
LINKEDIN_SEARCH = "https://www.linkedin.com/jobs/search/?keywords=fresher&location=Hyderabad%2C%20India&experience=0"

# ── Company Career Sites ──────────────────────────────────────────────
COMPANY_SITES = [
    {"name": "Accenture",   "url": "https://careers.accenture.com/jobs?location=Hyderabad&experience=Fresher"},
    {"name": "Wipro",       "url": "https://careers.wipro.com/jobs?location=Hyderabad&level=Fresher"},
    {"name": "TCS",         "url": "https://www.tcs.com/careers?location=Hyderabad&level=Fresher"},
    {"name": "Infosys",     "url": "https://www.infosys.com/careers?location=Hyderabad&level=Fresher"},
]
