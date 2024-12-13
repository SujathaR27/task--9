"""
PROGRAM : PYTEST FILE TO VALIDATE URL AND TITLE FROM Homepage.py
DATE : 13-NOV-2024
DEPENDANCIES : Homepage.py
"""

import pytest
from Homepage import SujathaAutomationCodes

url = "https://www.saucedemo.com/inventory.html"

sujatha = SujathaAutomationCodes(url)



#positive test case : validate url
def test_positive_url():
    test_url = "https://www.saucedemo.com/inventory.html"
    assert sujatha.fetch_url() == test_url
    print(f"SUCCESS : {test_url} is the valid URL")

#positive test case : validate title
def test_positive_title():
    test_title = "Swag Labs"
    assert sujatha.fetch_Title() == test_title
    print(f"SUCCESS : {test_title} is the valid Title")

#negative test case : validate url
def test_negative_url():
    test_url = ("https://www.guvi.in")
    assert sujatha.fetch_url() == test_url
    print(f"SUCCESS : {test_url} is the valid url")

#negative test case : validate title
def test_negative_ttile():
    test_title = "GUVI | LEAARN CODE"
    assert sujatha.fetch_Title() == test_title
    print(f"SUCCESS : {test_title} is the valid title")
