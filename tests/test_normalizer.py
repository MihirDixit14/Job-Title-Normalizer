import pytest
import json
from app.normalizer import normalize_title, FLAT_SYNONYMS

@pytest.mark.parametrize(
    "input_title,expected",
    [
        ("SWE","Software Engineer"),
        ("Software Engr","Software Engineer"),
        ("Sr. SWE", "Senior Software Engineer"),
        ("Senior Developer", "Senior Software Engineer"),
        ("PM", "Product Manager"),
        ("Prod Manager", "Product Manager"),
        
        ("unknown title", "unknown title"),
        ("Data Analyst", "Data Scientist"),
        ("Software Developer", "Software Engineer"),
        ("s/w engineer ", "Software Engineer"),
        ("Sofware Enginer", "Software Engineer"),  
        ("Sr. SWE", "Senior Software Engineer"),    
        ("Data anylist", "Data Scientist"),        
        ("product owne", "Product Manager"), 
        ("ml", "ML Engineer")
     
        
    ]
)



def test_normalize_title(input_title, expected):
    assert normalize_title(input_title)==expected

def test_non_string_input():
    with pytest.raises(AttributeError):
        normalize_title(None)
    with pytest.raises(AttributeError):

        normalize_title(["ML Engineer"])

def test_all_titles_and_synonyms():
    with open("app/job_titles.json") as f:

        mapping = json.load(f)
    for canonical, synonyms in mapping.items():

        for synonym in synonyms:
            result = normalize_title(synonym)
            if result != canonical:
                print(f"FAIL: '{synonym}' -> '{result}' (expected '{canonical}')")
    
