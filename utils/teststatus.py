from utils.custom_logger import customLogger as cl
import logging
from base.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):
    log = cl(logging.INFO)
    def __init__(self, driver, wait):
        #super(TestStatus, self).__init__(driver)
        self.driver = driver
        self.wait = wait
        self.resultList = []

    def setResult(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("#### Verification Successful #### %s", resultmessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.info("#### Verification Fails #### %s", resultmessage)
            else:
                self.resultList.append("Fail")
                self.log.error("#### Verification Fails #### %s", resultmessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("Exception Occurs !!!")


    def mark(self, result, resultmessage):
        self.setResult(result, resultmessage)

    def markFinal(self, testname, result, resultmessage):
        self.setResult(result, resultmessage)
        if "FAIL" in self.resultList:
            self.log.error(testname, "%s : ### TEST FAILED ###")
            self.resultList.clear()
            assert False
        else:
            self.log.info(testname, "%s : ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True