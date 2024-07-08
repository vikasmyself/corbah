'''
import unittest
from tests.test_login import TestLogin
from tests.test_addcart import AddCartPage

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(AddCartPage)

smoketest = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbose=2).run(smoketest)
'''
import unittest
from tests.test_login import TestLogin
from tests.test_addcart import TestAddCart
# Import other test classes as needed

# Create a test suite
def create_test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestLogin))
    test_suite.addTest(unittest.makeSuite(TestAddCart))
    # Add other test classes to the suite as needed
    return test_suite

if __name__ == "__main__":
    my_suite = create_test_suite()
    unittest.TextTestRunner(verbosity=2).run(my_suite)
