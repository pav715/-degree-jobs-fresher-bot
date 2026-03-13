# Create Separate Bots for B.Tech & M.Tech

## Current Bot Status

**Bot 1: General Fresher Jobs** ✅
- Location: `C:\1 API's work\Test 24\Degree Jobs Fresher\`
- Keywords: ANY degree (B.Sc, B.Com, MBA, etc.)
- Channel: `Degree Jobs Fresher-Hyd`
- Check interval: 10 minutes

---

## Template: B.Tech Fresher Bot

### Folder Setup
```
C:\1 API's work\Test 24\B.Tech Fresher
```

### config.py Keywords
```python
KEYWORDS = [
    # ── B.Tech Focus ──
    "B.Tech",
    "B.Tech Fresher",
    "Bachelor of Technology",
    "B.E",

    # ── Specializations ──
    "Computer Science",
    "Electronics",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Chemical Engineering",
    "Biotechnology",
    "Instrumentation",

    # ── Fresher Keywords ──
    "Fresher",
    "Entry Level",
    "Graduate Trainee",
    "Campus Hire",
    "0-1 years experience",
    "Recent Graduate",

    # ── Roles ──
    "Graduate Engineer",
    "Associate Engineer",
    "Trainee Engineer",
    "Junior Developer",
    "Junior Engineer",
]
```

### config.py Locations
```python
LOCATIONS = [
    "Hyderabad",
    "Hyderabad India",
    "Telangana",
    "Secunderabad",
    "Cyberabad",
]
```

### Telegram Channel
- Create channel: `B.Tech Fresher Jobs-Hyd`
- Add bot: `@USTaxjobs_bot` as Admin
- Get CHAT_ID and update config.py

---

## Template: M.Tech Fresher Bot

### Folder Setup
```
C:\1 API's work\Test 24\M.Tech Fresher
```

### config.py Keywords
```python
KEYWORDS = [
    # ── M.Tech Focus ──
    "M.Tech",
    "M.Tech Fresher",
    "Master of Technology",
    "M.E",

    # ── Specializations ──
    "Computer Science",
    "Electronics",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Data Science",
    "Biotechnology",

    # ── Fresher Keywords ──
    "Fresher",
    "Entry Level",
    "Graduate Trainee",
    "Campus Hire",
    "0-1 years experience",
    "Recent Graduate",

    # ── Roles ──
    "Graduate Engineer",
    "Associate Engineer",
    "Trainee Engineer",
    "Junior Developer",
    "Junior Engineer",
    "Data Analyst",
]
```

### config.py Locations
```python
LOCATIONS = [
    "Hyderabad",
    "Hyderabad India",
    "Telangana",
    "Secunderabad",
    "Cyberabad",
]
```

### Telegram Channel
- Create channel: `M.Tech Fresher Jobs-Hyd`
- Add bot: `@USTaxjobs_bot` as Admin
- Get CHAT_ID and update config.py

---

## Quick Setup Steps

### For B.Tech Bot:
1. Copy entire folder: `Degree Jobs Fresher` → `B.Tech Fresher`
2. Update `config.py` KEYWORDS (B.Tech only)
3. Create Telegram channel: `B.Tech Fresher Jobs-Hyd`
4. Get CHAT_ID and update config.py
5. Run: `python bot.py`

### For M.Tech Bot:
1. Copy entire folder: `Degree Jobs Fresher` → `M.Tech Fresher`
2. Update `config.py` KEYWORDS (M.Tech only)
3. Create Telegram channel: `M.Tech Fresher Jobs-Hyd`
4. Get CHAT_ID and update config.py
5. Run: `python bot.py`

---

## Summary

| Bot | Channel | Keywords | Status |
| :--- | :--- | :--- | :--- |
| General Fresher | `Degree Jobs Fresher-Hyd` | Any degree (no B.Tech/M.Tech) | ✅ Running |
| B.Tech Fresher | `B.Tech Fresher Jobs-Hyd` | B.Tech only | 📋 Template Ready |
| M.Tech Fresher | `M.Tech Fresher Jobs-Hyd` | M.Tech only | 📋 Template Ready |

All bots check every 10 minutes and post to Hyderabad/Telangana only!
