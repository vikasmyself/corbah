import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from utils.customer_parser import *
from pages.login_page import LoginPage
import pytest
from utils.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetup")
class TestLogin(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.driver = oneTimeSetup
        self.wait = WebDriverWait(self.driver,10)
        self.lp = LoginPage(self.driver, self.wait)
        self.ts = TestStatus(self.driver, self.wait)

    def test_login(self):
        uname = getConfig("login_page", "username")
        pword = getConfig("login_page", "password")
        self.lp.test_login(uname, pword)
        result1 = self.lp.test_verifylogin()
        self.ts.mark(result1,"Title Verified")

        self.lp.test_login(" "," ")
        result2 = self.lp.test_verifylogin()
        self.ts.markFinal("test_login", result2, "Login was successful")