from Pages.base_page_object import BasePage
from Locators.locators import CheckoutStepOneLocators
from TestData.TestData import TestData
import logging

class CheckoutStepOne(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def addcode(self, firstname, lastname, zipcode):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_zipcode(zipcode)

    def enter_firstname(self, firstname):
        message = "Enter the username '{}'"
        logging.info(message.format(firstname))
        self.enter_text(CheckoutStepOneLocators.INPUT_FIRSTNAME, firstname)

    def enter_lastname(self, lastname):
        message = "Enter the username '{}'"
        logging.info(message.format(lastname))
        self.enter_text(CheckoutStepOneLocators.INPUT_LASTNAME, lastname)

    def enter_zipcode(self, zipcode):
        message = "Enter the username '{}'"
        logging.info(message.format(zipcode))
        self.enter_text(CheckoutStepOneLocators.INPUT_ZIPCODE, zipcode)

    def click_continute(self):
        logging.info("click continute")
        self.click(CheckoutStepOneLocators.CONTINUTE_BUTTON)

    def click_cancel_button(self):
        logging.info("finish button")
        self.click(CheckoutStepOneLocators.CANCEL_BUTTON_1)
