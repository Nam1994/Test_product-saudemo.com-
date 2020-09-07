from Pages.base_page_object import BasePage
from Locators.locators import CheckoutStepTwoLocators
from TestData.TestData import TestData
import logging

class CheckoutStepTwo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_finish_button(self):
        logging.info("finish button")
        self.click(CheckoutStepTwoLocators.FINISH_BUTTON)

    def cancel_button_2(self):
        logging.info("finish button")
        self.click(CheckoutStepTwoLocators.CANCEL_BUTTON_2)