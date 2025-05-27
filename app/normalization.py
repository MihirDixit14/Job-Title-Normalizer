import json
from typing import Dict
from rapidfuzz import fuzz, process 
from pathlib import Path

CANONICAL_FILE=Path(__file__).parent/"job_titles.json"
def load_titles()-> Dict[str,list]:
    with open(CANONICAL_FILE,"r") as f:
        return json.load(f)
TITLES=load_titles
FLAT_SYNONYMS={}
for canonical, synonyms in TITLES.items():
    FLAT_SYNONYMS[canonical]=canonical
    for synonym in synonyms:
        FLAT_SYNONYMS[synonym.lower()] = canonical

def normalize_title(input_title:str)->str:
    title_clean=input_title.strip().lower()
    if title_clean in FLAT_SYNONYMS:
        return FLAT_SYNONYMS[title_clean]
    all_titles=list(FLAT_SYNONYMS.keys())
    match, score=process.extractOne(title_clean,scorer=fuzz.partial_token_sort_ratio)
    if score>80:
        return FLAT_SYNONYMS[match]
    return input_title
                                        