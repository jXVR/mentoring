from unittest import defaultTestLoader
from unittest import TextTestRunner
from Selenium_Tests.Test_Cases.Sign_up_test import SignUpTest
from Selenium_Tests.Test_Cases.Login_test import LoginTest
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-b", "--browser", default="Chrome")
args = arg_parser.parse_args()

LoginTest.browser = args.browser
# SignUpTest.browser = args.browser
# zmienic browser w kazdym pliku z testami

if __name__ == "__main__":
    TextTestRunner(verbosity=2).run(defaultTestLoader.loadTestsFromTestCase(SignUpTest))
    TextTestRunner(verbosity=2).run(defaultTestLoader.loadTestsFromTestCase(LoginTest))brew install postgresql