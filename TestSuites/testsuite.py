import sys
sys.path.append(".")
import unittest
from TestCases.test_case_02 import HerokuAppLogin2
from TestCases.test_case_03 import HerokuAppLogin3
from TestCases.test_case_04 import HerokuAppLogin4

# get all tests from Login class
login2 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin2)
login3 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin3)
login4 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin4)

# create a test suite
test_suite = unittest.TestSuite([ login2, login3, login4])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)