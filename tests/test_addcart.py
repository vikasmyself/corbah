import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from pages.addcart_page import AddCartPage
import pytest


@pytest.mark.usefixtures("oneTimeSetup")
class TestAddCart(unittest.TestCase):

    def test_login(self):
        lp1 = AddCartPage(self.driver, self.wait)
        lp1.test_addcart()