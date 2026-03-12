"""
Job scraper — LinkedIn + Google Jobs + Workday + India Portals
Filters for: Freshers Only, Hyderabad & Telangana, All Degree Types (UG/PG)
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import requests
import hashlib
import re
import time
import random
from datetime import datetime
from urllib.parse import urljoin, quote
from bs4 import BeautifulSoup
import config

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
})

PRIORITY_KEYWORDS = [
    "Fresher",
    "Entry Level",
    "Graduate",
    "B.Tech",
    "M.Tech",
    "BCA",
    "MCA",
]

FRESHER_PATTERN = re.compile(
    r"\b(fresher|entry\s*level|graduate|new\s*graduate|recent\s*graduate|"
    r"campus\s*hire|trainee|0\s*years|less\s*than\s*1\s*year|first\s*job)\b",
    re.IGNORECASE,
)

DEGREE_PATTERN = re.compile(
    r"\b(degree|graduate|bachelor|master|diploma|b\.?a|b\.?sc|m\.?sc|b\.?com|mba|bca|mca)\b",
    re.IGNORECASE,
)

LOCATION_PATTERN = re.compile(
    r"\b(hyderabad|hyd|telangana|secunderabad|cyberabad)\b",
    re.IGNORECASE,
)


def job_id(url, title, company):
    raw = f"{url}{title}{company}".lower().strip()
    return hashlib.md5(raw.encode()).hexdigest()[:16]


def _delay():
    time.sleep(random.uniform(0.2, 0.5))  # Reduced for GitHub Actions


def _is_fresher_job(title, description):
    """Check if job is for freshers."""
    text = f"{title} {description}".lower()
    return bool(FRESHER_PATTERN.search(text))


def _has_degree_keyword(title, description):
    """Check if job mentions degrees."""
    text = f"{title} {description}".lower()
    return bool(DEGREE_PATTERN.search(text))


def _has_location(location_str):
    """Check if location contains Hyderabad/Telangana."""
    if not location_str:
        return False
    return bool(LOCATION_PATTERN.search(location_str))


# ── LinkedIn Jobs (via search + Google scrape simulation) ──────────────
def fetch_linkedin_jobs():
    """
    LinkedIn jobs search for freshers in Hyderabad.
    Note: Direct LinkedIn scraping may require Selenium for dynamic content.
    This is a placeholder for API/manual search results.
    """
    jobs = []
    try:
        # LinkedIn URL with fresher + Hyderabad filters
        url = "https://www.linkedin.com/jobs-guest/jobs/api/jobPosting?keywords=fresher&location=Hyderabad&experience=0"

        r = SESSION.get(url, timeout=15)
        if r.status_code != 200:
            return jobs

        data = r.json() if r.headers.get('content-type') == 'application/json' else []

        for item in data if isinstance(data, list) else []:
            try:
                job_url = item.get("jobUrl", "")
                title = item.get("title", "")
                company = item.get("companyName", "")
                location = item.get("location", "")
                description = item.get("description", "")
                posted_date = item.get("postedDate", "")

                if not title or not company:
                    continue

                if not _is_fresher_job(title, description):
                    continue

                if not _has_location(location):
                    continue

                job = {
                    "id": job_id(job_url, title, company),
                    "title": title,
                    "company": company,
                    "location": location,
                    "url": job_url,
                    "source": "LinkedIn",
                    "description": description,
                    "posted": posted_date,
                }
                jobs.append(job)
                _delay()
            except Exception:
                continue

    except Exception as e:
        print(f"LinkedIn scrape error: {e}")

    return jobs


# ── Google Jobs API (via search) ──────────────────────────────────────
def fetch_google_jobs():
    """
    Google Jobs search for freshers in Hyderabad.
    """
    jobs = []
    try:
        # Google Jobs search URL
        search_query = "fresher site:google.com/careers"
        url = f"https://www.google.com/search?q={quote(search_query)}&location=Hyderabad"

        r = SESSION.get(url, timeout=15)
        if r.status_code != 200:
            return jobs

        soup = BeautifulSoup(r.content, "html.parser")

        for item in soup.find_all("div", class_="g"):
            try:
                title_elem = item.find("h3")
                if not title_elem:
                    continue

                title = title_elem.get_text(strip=True)
                link_elem = item.find("a", href=True)
                job_url = link_elem["href"] if link_elem else ""

                if not _is_fresher_job(title, ""):
                    continue

                job = {
                    "id": job_id(job_url, title, "Google"),
                    "title": title,
                    "company": "Google",
                    "location": "Hyderabad",
                    "url": job_url,
                    "source": "Google Jobs",
                    "description": "",
                    "posted": datetime.now().isoformat(),
                }
                jobs.append(job)
                _delay()
            except Exception:
                continue

    except Exception as e:
        print(f"Google Jobs scrape error: {e}")

    return jobs


# ── India Job Portals (HTML scrape) ──────────────────────────────────
def fetch_india_portal_jobs():
    """
    Scrape Naukri, Foundit, Shine, TimesJobs for fresher jobs in Hyderabad.
    """
    jobs = []

    for portal in config.INDIA_PORTALS:
        try:
            r = SESSION.get(portal["url"], timeout=15)
            if r.status_code != 200:
                continue

            soup = BeautifulSoup(r.content, "html.parser")

            # Generic job card selector (varies by portal)
            for card in soup.find_all(["div", "article"], class_=re.compile(r"job|card|listing")):
                try:
                    title_elem = card.find(["h1", "h2", "h3", "a"])
                    if not title_elem:
                        continue

                    title = title_elem.get_text(strip=True)
                    company_elem = card.find(["span", "p"], class_=re.compile(r"company|employer"))
                    company = company_elem.get_text(strip=True) if company_elem else "Unknown"

                    location_elem = card.find(["span", "p"], class_=re.compile(r"location|place"))
                    location = location_elem.get_text(strip=True) if location_elem else ""

                    link_elem = card.find("a", href=True)
                    job_url = urljoin(portal["url"], link_elem["href"]) if link_elem else ""

                    description = card.get_text(strip=True)[:500]

                    if not title or not job_url:
                        continue

                    if not _is_fresher_job(title, description):
                        continue

                    if not _has_location(location):
                        continue

                    job = {
                        "id": job_id(job_url, title, company),
                        "title": title,
                        "company": company,
                        "location": location,
                        "url": job_url,
                        "source": portal["name"],
                        "description": description,
                        "posted": datetime.now().isoformat(),
                    }
                    jobs.append(job)
                    _delay()
                except Exception:
                    continue

        except Exception as e:
            print(f"{portal['name']} scrape error: {e}")

    return jobs


# ── Workday ATS API (for companies like Accenture, Wipro, TCS, etc.) ────
def fetch_workday_jobs():
    """
    Fetch fresher jobs from Workday ATS (Accenture, Wipro, TCS, Infosys, etc.)
    """
    jobs = []

    for company in config.WORKDAY_COMPANIES:
        try:
            # Workday API endpoint
            url = (
                f"https://{company['tenant']}.wd{company['wd']}.myworkdayjobs.com/"
                f"wday/cxs/{company['tenant']}/{company['path']}/jobs"
            )

            payload = {
                "appliedFacets": {
                    "locationCountry": ["India"],
                    "experienceLevel": ["Fresher", "Entry Level"],
                },
                "limit": 100,
                "offset": 0,
            }

            r = SESSION.post(url, json=payload, timeout=15)
            if r.status_code != 200:
                continue

            data = r.json()
            for item in data.get("jobPostings", []):
                try:
                    title = item.get("title", "")
                    job_url = item.get("externalJobPostingUrl", "")
                    location = item.get("location", "")
                    description = item.get("description", "")

                    if not title or not job_url:
                        continue

                    if not _is_fresher_job(title, description):
                        continue

                    if not _has_location(location):
                        continue

                    job = {
                        "id": job_id(job_url, title, company["name"]),
                        "title": title,
                        "company": company["name"],
                        "location": location,
                        "url": job_url,
                        "source": "Workday",
                        "description": description,
                        "posted": item.get("postedDate", datetime.now().isoformat()),
                    }
                    jobs.append(job)
                except Exception:
                    continue

            _delay()
        except Exception as e:
            print(f"Workday {company['name']} error: {e}")

    return jobs


# ── Company Career Sites ─────────────────────────────────────────────
def fetch_company_sites():
    """
    Scrape company career sites (Accenture, Wipro, TCS, etc.)
    """
    jobs = []

    for company in config.COMPANY_SITES:
        try:
            r = SESSION.get(company["url"], timeout=15)
            if r.status_code != 200:
                continue

            soup = BeautifulSoup(r.content, "html.parser")

            for card in soup.find_all(["div", "article"], class_=re.compile(r"job|card|listing")):
                try:
                    title_elem = card.find(["h1", "h2", "h3", "a"])
                    if not title_elem:
                        continue

                    title = title_elem.get_text(strip=True)
                    link_elem = card.find("a", href=True)
                    job_url = urljoin(company["url"], link_elem["href"]) if link_elem else ""
                    description = card.get_text(strip=True)[:500]

                    if not title or not job_url:
                        continue

                    if not _is_fresher_job(title, description):
                        continue

                    job = {
                        "id": job_id(job_url, title, company["name"]),
                        "title": title,
                        "company": company["name"],
                        "location": "Hyderabad",
                        "url": job_url,
                        "source": "Company Site",
                        "description": description,
                        "posted": datetime.now().isoformat(),
                    }
                    jobs.append(job)
                    _delay()
                except Exception:
                    continue

        except Exception as e:
            print(f"{company['name']} site scrape error: {e}")

    return jobs


# ── Aggregate All Jobs ────────────────────────────────────────────────
def fetch_all_jobs():
    """
    Fetch from all sources and deduplicate by job ID.
    Return sorted by posted date (newest first).
    """
    all_jobs = []

    print("Fetching LinkedIn jobs...")
    all_jobs.extend(fetch_linkedin_jobs())

    print("Fetching Google Jobs...")
    all_jobs.extend(fetch_google_jobs())

    print("Fetching India Portal jobs...")
    all_jobs.extend(fetch_india_portal_jobs())

    print("Fetching Workday jobs...")
    all_jobs.extend(fetch_workday_jobs())

    print("Fetching Company Site jobs...")
    all_jobs.extend(fetch_company_sites())

    # Deduplicate by ID
    seen_ids = set()
    unique_jobs = []
    for job in all_jobs:
        if job["id"] not in seen_ids:
            seen_ids.add(job["id"])
            unique_jobs.append(job)

    # Sort by posted date (newest first)
    unique_jobs.sort(
        key=lambda x: x.get("posted", ""),
        reverse=True
    )

    return unique_jobs
