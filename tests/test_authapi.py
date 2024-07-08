from utils.customer_parser import *
from base.api_driver import ApiDriver

class TestAuthAPI:
    def test_authapi(self):
        self.url = getConfig("Bex_API","auth_url")
        api_driver = ApiDriver(self.url)
        api_driver.authAPI()