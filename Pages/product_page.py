from Pages.base_page_object import BasePage
from Locators.locators import ProductLocators
import logging

class ProductPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)

  def add_product_to_cart(self, index):
   # print("Productpage:" + str(index))
    self.click(ProductLocators.ADD_TO_CART_BUTTON(index))

  def click_bag_icon(self):
      logging.info("ADD a cart")
      self.click(ProductLocators.CLICK_BAG)

  def remove_add_to_cart(self, index):
   # print("Productpage:" + str(index))
    self.click(ProductLocators.REMOVE_TO_CART_BUTTON())













