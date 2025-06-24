# tests/test_scraper.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scraper.parsers import get_star_rating

import pytest
from scraper.parsers import get_star_rating

@pytest.mark.parametrize("class_string,expected", [
    ("star-rating One", 1),
    ("star-rating Two", 2),
    ("star-rating Three", 3),
    ("star-rating Four", 4),
    ("star-rating Five", 5),
    ("star-rating Zero", 0),
])
def test_get_star_rating(class_string, expected):
    assert get_star_rating(class_string) == expected

