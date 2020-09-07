import sys
sys.path.append(".")
import unittest
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.checkout_step_one_page import CheckoutStepOne
from Pages.checkout_step_two_page import CheckoutStepTwo
from TestCases.base_test import BaseTest
from TestData.TestData import TestData
import time

class HerokuAppLogin2(BaseTest):
    """A sample test class to show how page object works"""
    @classmethod
    def setUp(self):
        super().setUp(TestData.BROWSER)

    @classmethod
    def tearDown(self):
         super().tearDown()

    def test_login_successfully(self):
        login_page = LoginPage(self.driver)
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        product_page = ProductPage(self.driver)
        product_page.add_product_to_cart(1)
        product_page.add_product_to_cart(2)
        product_page.add_product_to_cart(3)
        product_page.click_bag_icon()
        time.sleep(2)
        cart_page = CartPage(self.driver)
        cart_page.remove_product_to_cart_in_bag(1)
        time.sleep(2)
        cart_page.click_checkout()
        checkout_step_one_page = CheckoutStepOne(self.driver)
        checkout_step_one_page.addcode(TestData.FIRSTNAME, TestData.LASTNAME, TestData.ZIPCODE)
        checkout_step_one_page.click_continute()
        checkout_step_two_page = CheckoutStepTwo(self.driver)
        checkout_step_two_page.click_finish_button()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
