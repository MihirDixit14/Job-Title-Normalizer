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

                                        