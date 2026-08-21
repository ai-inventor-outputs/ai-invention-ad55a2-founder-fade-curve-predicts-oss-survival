#!/usr/bin/env python3
"""Fetch BibTeX entries from Semantic Scholar API directly."""
import json
import time
import re
import requests
from typing import Optional

HEADERS = {"User-Agent": "AI-Inventor-Paper/1.0"}

def fetch_by_doi(doi: str) -> Optional[dict]:
    """Fetch paper metadata by DOI."""
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}"
    params = {"fields": "title,authors,year,venue,abstract,externalIds,journal"}
    try:
        r = requests.get(url, params=params, headers=HEADERS, timeout=30)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        print(f"  Error fetching DOI {doi}: {e}")
    return None

def fetch_by_arxiv(arxiv_id: str) -> Optional[dict]:
    """Fetch paper metadata by ArXiv ID."""
    url = f"https://api.semanticscholar.org/graph/v1/paper/ArXiv:{arxiv_id}"
    params = {"fields": "title,authors,year,venue,abstract,externalIds,journal"}
    try:
        r = requests.get(url, params=params, headers=HEADERS, timeout=30)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        print(f"  Error fetching ArXiv {arxiv_id}: {e}")
    return None

def fetch_by_title(title: str, author: str = None) -> Optional[dict]:
    """Fetch paper metadata by title search."""
    url = "https://api.semanticscholar.org/graph/v1/paper/search/match"
    params = {
        "title": title,
        "fields": "title,authors,year,venue,abstract,externalIds,journal",
        "year": "",
    }
    if author:
        params["author"] = author
    try:
        r = requests.get(url, params=params, headers=HEADERS, timeout=30)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        print(f"  Error fetching title '{title}': {e}")
    return None

def make_citation_key(authors: list, year: int) -> str:
    """Create citation key from first author and year."""
    if not authors:
        return f"Unknown{year}"
    first = authors[0]
    if isinstance(first, dict):
        name = first.get("name", "Unknown")
    else:
        name = str(first)
    # Extract last name
    parts = name.split()
    last = parts[-1] if parts else "Unknown"
    last = re.sub(r'[^A-Za-z]', '', last)
    return f"{last}{year}"

def to_bibtex(data: dict, citation_key: str = None) -> str:
    """Convert Semantic Scholar JSON to BibTeX."""
    title = data.get("title", "Unknown Title")
    authors_raw = data.get("authors", [])
    year = data.get("year", "????")
    venue = data.get("venue", "")
    journal = data.get("journal", {})
    abstract = data.get("abstract", "")
    external_ids = data.get("externalIds", {})

    # Determine entry type
    if journal and journal.get("name"):
        entry_type = "article"
        journal_name = journal.get("name", "")
        volume = journal.get("volume", "")
        number = journal.get("number", "")
        pages = journal.get("pages", "")
    elif venue:
        if any(kw in venue.lower() for kw in ["proceedings", "conference", "workshop"]):
            entry_type = "inproceedings"
        else:
            entry_type = "article"
        journal_name = venue
        volume = ""
        number = ""
        pages = ""
    else:
        entry_type = "misc"
        journal_name = ""
        volume = ""
        number = ""
        pages = ""

    # Format authors
    author_str = " and ".join(
        a.get("name", "") if isinstance(a, dict) else str(a)
        for a in authors_raw
    )

    # Citation key
    if citation_key is None:
        citation_key = make_citation_key(authors_raw, year)

    # Build BibTeX
    lines = [f"@{entry_type}{{{citation_key},"]
    lines.append(f"  title = {{{title}}},")
    if author_str:
        lines.append(f"  author = {{{author_str}}},")
    lines.append(f"  year = {{{year}}},")
    if journal_name:
        lines.append(f"  journal = {{{journal_name}}},")
    if volume:
        lines.append(f"  volume = {{{volume}}},")
    if number:
        lines.append(f"  number = {{{number}}},")
    if pages:
        lines.append(f"  pages = {{{pages}}},")
    if external_ids.get("DOI"):
        lines.append(f"  doi = {{{external_ids['DOI']}}},")
    if external_ids.get("ArXiv"):
        lines.append(f"  arxiv = {{{external_ids['ArXiv']}}},")
    lines.append("}")
    return "\n".join(lines)

# References to fetch
refs = [
    {"doi": "10.1109/esem.2019.8870181", "author": "Avelino", "year": 2019,
     "key": "Avelino2019"},
    {"doi": "10.1016/j.jss.2026.112942", "author": "Kaushik", "year": 2026,
     "key": "Kaushik2026"},
    {"doi": "10.1111/j.1469-7610.1976.tb00381.x", "author": "Wood", "year": 1976,
     "key": "Wood1976"},
    {"doi": "10.1109/icse.2019.00078", "author": "Wang", "year": 2019,
     "key": "Wang2019"},
    {"doi": "10.1007/s10664-021-10012-6", "author": "Kamei", "year": 2022,
     "key": "Kamei2022"},
    {"doi": "10.1145/3236024.3236062", "author": "Gousios", "year": 2018,
     "key": "Gousios2018"},
    {"doi": "10.1007/s10515-026-00634-9", "author": "Zhang", "year": 2026,
     "key": "Zhang2026"},
    {"doi": "10.1145/3555190", "author": "Klimke", "year": 2022,
     "key": "Klimke2022"},
]

bib_entries = []

for i, ref in enumerate(refs):
    print(f"Fetching {i+1}/{len(refs)}: {ref.get('title', ref.get('doi', 'unknown'))}")
    data = None

    if "doi" in ref:
        data = fetch_by_doi(ref["doi"])
        time.sleep(0.5)
    
    if data is None and "title" in ref:
        data = fetch_by_title(ref["title"], ref.get("author"))
        time.sleep(1.0)

    if data and data.get("title"):
        key = ref.get("key", make_citation_key(data.get("authors", []), data.get("year", 2000)))
        bibtex = to_bibtex(data, key)
        bib_entries.append(bibtex)
        print(f"  -> Got: {data['title'][:60]}")
    else:
        print(f"  -> FAILED")

# Write to file
output = "\n\n".join(bib_entries)
with open("references.bib", "w") as f:
    f.write(output)

print(f"\nWrote {len(bib_entries)} entries to references.bib")
