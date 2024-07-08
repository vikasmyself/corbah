from base.selenium_driver import SeleniumDriver
import time
class AddCartPage(SeleniumDriver):
    def __init__(self,driver,wait):
        super(AddCartPage, self).__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        self.collection_xpath = "//li[@class='header-menu__list-item'][1]/a"
        self.allitems_xpath = "//div[@class='list-colletions max-w-screen mx-auto']//div[2]//div[2]"
        self.checkbox_bibshort_xpath = "//input[@value='Bib Shorts']"
        self.filter_bibshort_xpath = "//a[@class='active-filter active-filter__remove-filter']"
        self.select_item_xpath = "//div[@id='ProductGridContainer']//li[4]/div"
        self.close_dialog_xpath = "//div[@class='ep_featherlight']/div/span[contains(@class,'ep_featherlight-close-ic')]"
        self.select_size_xpath = "//div[@class='product__variants product__variants--radio']//label[4]"
        self.addcart_xpath = "//button[@name='add']"
        self.itemadded_dialog_xpath = "//div[@id='cart-notification-links']"
        self.itemadded_dialog_close_xpath = "//div[@class='cart-notification__title']/button"
        self.viewcart_xpath = "//a[@id='cart-button']"
        self.checkbox_cart_agreement_xpath = "//input[@id='Cart-Agreement']"
        self.checkbox_checkout_xpath = "//input[@id='effectiveAppsAgreeCB']"
        self.checkout_xpath = "//*[@id='main-cart-footer']/div/div/div/div[2]/div[1]/button"
        self.delivery_appears_xpath = "//h2[contains(text(),'Delivery')]"

    def test_addcart(self):
        self.elementClick(self.collection_xpath, locatorType="xpath")
        self.elementClick(self.allitems_xpath, locatorType="xpath")
        title = self.getTitle()
        print("*" * 20)
        print(title)
        self.elementClick(self.checkbox_bibshort_xpath,locatorType="xpath")
        self.isElementPresent(self.filter_bibshort_xpath, locatorType="xpath")
        self.screenShot("Bib Short")
        self.elementClick(self.select_item_xpath, locatorType="xpath")
        self.isElementPresent(self.close_dialog_xpath, locatorType="xpath")
        self.elementClick(self.close_dialog_xpath, locatorType="xpath")
        self.waitForElement(self.select_size_xpath,locatorType="xpath",timeout=2)
        self.elementClick(self.select_size_xpath, locatorType="xpath")
        self.waitForElement(self.addcart_xpath, locatorType="xpath",timeout=2)
        self.elementClick(self.addcart_xpath, locatorType="xpath")
        self.waitForElement(self.itemadded_dialog_xpath, locatorType="xpath",timeout=2)
        self.isElementPresent(self.itemadded_dialog_xpath, locatorType="xpath")
        self.waitForElement(self.itemadded_dialog_close_xpath, locatorType="xpath",timeout=2)
        self.elementClick(self.itemadded_dialog_close_xpath, locatorType="xpath")
        self.waitForElement(self.viewcart_xpath, locatorType="xpath",timeout=2)
        self.elementClick(self.viewcart_xpath, locatorType="xpath")
        checkbox = self.waitForElement(self.checkbox_cart_agreement_xpath, locatorType="xpath",pollFrequency=3)
        self.elementClick(element=checkbox)
        another_checkbox = self.waitForElement(self.checkbox_checkout_xpath, locatorType="xpath",pollFrequency=2)
        self.elementClick(another_checkbox)
        checkout = self.waitForElement(self.checkout_xpath, locatorType="xpath",pollFrequency=2)
        self.elementClick(checkout)
        self.isElementPresent(self.delivery_appears_xpath, locatorType="xpath")
        self.screenShot("Smile.. End of Test")


