"""
Homepage.py

PROGRAM : Python Selenium Automation Codes
DATE : 13-NOV-2024
"""

from selenium import webdriver
from selenium.webdriver. chrome. service import Service
from webdriver_manager. chrome import ChromeDriverManager
from time import sleep



class SujathaAutomationCodes:

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(). install()))

        """The automation start method"""
    def start(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True
        except Exception as error:
            print("Error : Unable to start python selenium automation!", error)
            return False

        """The automation shutdown method"""
    def shutdown(self):
        self.driver.quit()

        """The method to fetch url of web page"""
    def fetch_url(self):
        if self.start():
            return self.driver.current_url
        else:"ERROR : Unable to fetch url !"

        """The method to fetch title of web page"""
    def fetch_Title(self):
            if self.start():
                return self.driver.title
            else:"ERROR : Unable to fetch Title"




