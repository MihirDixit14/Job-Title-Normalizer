import pytest
from app.normalizer import normalize_title

@pytest.mark.parametrize(
    "input_title,expected",
    [
        ("SWE","Software Engineer"),
        ("Software Engr","Software Engineer"),
        ("Sr. SWE", "Senior Software Engineer"),
        ("Senior Developer", "Senior Software Engineer"),
        ("PM", "Product Manager"),
        ("Prod Manager", "Product Manager"),
        ("ML Engineer", "Data Scientist"),
        ("unknown title", "unknown title"),
          ("Data Analyst", "Data Scientist"),
        ("Software Developer", "Software Engineer"),
        ("s/w engineer ", "Software Engineer"),
    ]
)

def test_normalize_title(input_title, expected):
    assert normalize_title(input_title)==expected
