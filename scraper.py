"""
Job scraper — Degree Jobs Fresher
Sources: Naukri API, LinkedIn public API, Indeed RSS
"""
import requests
import hashlib
import re
import time
import random
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import config

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def job_id(url, title, company):
    """Unique fingerprint for a job — used to detect duplicates."""
    raw = f"{url}{title}{company}".lower().strip()
    return hashlib.md5(raw.encode()).hexdigest()[:16]


def delay():
    time.sleep(random.uniform(0.2, 0.5))


# ── LINKEDIN (public API) ──────────────────────────────────────────
def scrape_linkedin(keyword, location):
    jobs = []
    try:
        kw  = keyword.replace(" ", "%20")
        loc = location.replace(" ", "%20")
        url = (
            f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?"
            f"keywords={kw}&location={loc}&f_TPR=r604800"
            f"&sortBy=DD&start=0"
        )
        r    = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")
        for card in soup.find_all("li")[:20]:
            try:
                title   = card.find("h3").get_text(strip=True) if card.find("h3") else ""
                company = card.find("h4").get_text(strip=True) if card.find("h4") else ""
                loc_tag = card.find("span", class_=re.compile("job-search-card__location"))
                loc_str = loc_tag.get_text(strip=True) if loc_tag else location
                link_tag = card.find("a", href=True)
                link    = link_tag["href"].split("?")[0] if link_tag else ""
                time_tag = card.find("time")
                posted  = time_tag["datetime"] if time_tag and time_tag.get("datetime") else ""

                if not title or not link:
                    continue

                jobs.append({
                    "id":       job_id(link, title, company),
                    "title":    title,
                    "company":  company,
                    "location": loc_str,
                    "url":      link,
                    "posted":   posted,
                    "source":   "LinkedIn",
                    "fetched_at": datetime.now().isoformat(),
                })
            except Exception:
                pass
    except Exception as e:
        print(f"  [LinkedIn] Error ({keyword}/{location}): {e}")
    return jobs


# ── NAUKRI API ─────────────────────────────────────────────────────
def scrape_naukri(keyword, location):
    jobs = []
    try:
        kw  = keyword.replace(" ", "%20")
        loc = location.replace(" ", "%20")
        url = (
            f"https://www.naukri.com/jobapi/v3/search?"
            f"noOfResults=20&urlType=search_by_keyword&searchType=adv"
            f"&keyword={kw}&location={loc}&experience=0"
            f"&jobAge=7&src=jobsearchDesk&latLong="
        )
        r = requests.get(url, headers={**HEADERS, "appid": "109", "systemid": "109"}, timeout=10)
        data = r.json()
        for j in data.get("jobDetails", []):
            title   = j.get("title", "").strip()
            company = j.get("companyName", "").strip()
            loc_str = location
            jurl    = f"https://www.naukri.com{j.get('jdURL', '')}"
            posted  = j.get("footerPlaceholderLabel", "")

            if not title or not jurl:
                continue

            jobs.append({
                "id":       job_id(jurl, title, company),
                "title":    title,
                "company":  company,
                "location": loc_str,
                "url":      jurl,
                "posted":   posted,
                "source":   "Naukri",
                "fetched_at": datetime.now().isoformat(),
            })
    except Exception as e:
        print(f"  [Naukri] Error ({keyword}/{location}): {e}")
    return jobs


# ── INDEED INDIA (RSS) ─────────────────────────────────────────────
def scrape_indeed(keyword, location):
    jobs = []
    try:
        kw  = keyword.replace(" ", "+")
        loc = location.replace(" ", "+")
        url = f"https://in.indeed.com/rss?q={kw}&l={loc}&sort=date&fromage=7"
        r   = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.content, "xml")
        for item in soup.find_all("item")[:15]:
            title   = item.find("title").get_text(strip=True) if item.find("title") else ""
            link    = item.find("link").get_text(strip=True) if item.find("link") else ""
            company_tag = item.find("source")
            company = company_tag.get_text(strip=True) if company_tag else "Unknown"
            pub_date = item.find("pubDate")
            posted  = pub_date.get_text(strip=True) if pub_date else ""

            if not title or not link:
                continue

            jobs.append({
                "id":       job_id(link, title, company),
                "title":    title,
                "company":  company,
                "location": location,
                "url":      link,
                "posted":   posted,
                "source":   "Indeed",
                "fetched_at": datetime.now().isoformat(),
            })
    except Exception as e:
        print(f"  [Indeed] Error ({keyword}/{location}): {e}")
    return jobs


# ── MAIN SCRAPE FUNCTION ──────────────────────────────────────────
def fetch_all_jobs(minutes_back=5):
    """
    Fetch fresher jobs from LinkedIn, Naukri, and Indeed.
    """
    all_jobs = []
    seen_urls = set()

    print(f"Fetching fresher jobs from LinkedIn, Naukri, Indeed...")

    # Try each keyword and location
    for keyword in config.KEYWORDS[:10]:  # Limit to first 10 keywords for speed
        for location in config.LOCATIONS:
            try:
                # LinkedIn
                results = scrape_linkedin(keyword, location)
                for job in results:
                    url = job.get("url", "")
                    if url and url not in seen_urls:
                        seen_urls.add(url)
                        all_jobs.append(job)
                delay()

                # Naukri
                results = scrape_naukri(keyword, location)
                for job in results:
                    url = job.get("url", "")
                    if url and url not in seen_urls:
                        seen_urls.add(url)
                        all_jobs.append(job)
                delay()

                # Indeed
                results = scrape_indeed(keyword, location)
                for job in results:
                    url = job.get("url", "")
                    if url and url not in seen_urls:
                        seen_urls.add(url)
                        all_jobs.append(job)
                delay()

            except Exception as e:
                print(f"  Error fetching {keyword}/{location}: {e}")

    # Filter by time window
    now = datetime.now()
    cutoff_time = now - timedelta(minutes=minutes_back)
    recent_jobs = []

    for job in all_jobs:
        try:
            posted_str = job.get("posted", "")
            if not posted_str:
                recent_jobs.append(job)
                continue

            try:
                posted_time = datetime.fromisoformat(posted_str.replace('Z', '+00:00'))
            except Exception:
                try:
                    posted_time = datetime.fromisoformat(posted_str)
                except Exception:
                    recent_jobs.append(job)
                    continue

            if posted_time >= cutoff_time:
                recent_jobs.append(job)
        except Exception:
            recent_jobs.append(job)

    # Deduplicate
    seen_ids = set()
    unique_jobs = []
    for job in recent_jobs:
        if job["id"] not in seen_ids:
            seen_ids.add(job["id"])
            unique_jobs.append(job)

    # Sort newest first
    unique_jobs.sort(key=lambda x: x.get("posted", ""), reverse=True)

    print(f"Found {len(unique_jobs)} fresher jobs")
    return unique_jobs
