from selenium.webdriver.support import wait
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):
    def __init__(self,driver,wait):
        super(LoginPage,self).__init__(driver,wait)
        self.driver = driver
        self.wait = wait
        self.home_login_xpath = "//div[@class='header-top__account']/a[contains(text(),'Log in')]"
        self.login_email_xpath = "//input[@id='CustomerForm-email']"
        self.login_password_xpath = "//input[@id='CustomerForm-password']"
        self.login_signin_xpath = "//*[@id='customer_login']/div/div[3]//button"
        self.logout_xpath = "//div[@class='header-top__account']//a[contains(text(),'Log out')]"


    def test_login(self, username, password):
        self.isElementPresent(self.home_login_xpath,locatorType="xpath")
        self.elementClick(self.home_login_xpath,locatorType="xpath")
        self.sendKeys(username, self.login_email_xpath, locatorType="xpath")
        self.sendKeys(password, self.login_password_xpath, locatorType="xpath")
        self.waitForElement(self.login_signin_xpath, locatorType="xpath", timeout=2)
        self.elementClick(self.login_signin_xpath, locatorType="xpath")
        self.screenShot("Smile.. Taking Screenshot")

    def test_verifylogin(self):
        temp = self.waitForElement(self.logout_xpath, locatorType="xpath", timeout=5)
        if temp:
            return True
        else:
            return False

