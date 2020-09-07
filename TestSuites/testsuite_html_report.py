import os
import sys

sys.path.append(".")
from Utils.HTMLTestRunner import *
from TestCases.test_case_02 import HerokuAppLogin2
from TestCases.test_case_03 import HerokuAppLogin3
from TestCases.test_case_04 import HerokuAppLogin4

# get the directory path to output report file
dir = os.getcwd()

# get all tests from Login class
login2 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin2)
login3 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin3)
login4 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin4)

# create a test suite
test_suite = unittest.TestSuite([login2, login3, login4])

# open the report file
outfile = open(dir + "/SeleniumPythonTestSummary.html", "w", encoding='utf-8')

# configure HTMLTestRunner options
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)
outfile.close()
