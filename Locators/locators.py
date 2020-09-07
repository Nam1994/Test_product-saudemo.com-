from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    INPUT_USERNAME = (By.ID, 'user-name')
    INPUT_PASSWORD = (By.ID, 'password')
    BUTTON_LOGIN = (By.XPATH, "//*[@id='login-button']")

class ProductLocators(object):
    CLICK_BAG = (By.XPATH, "//*[@class='shopping_cart_container']")

    def ADD_TO_CART_BUTTON(index):
        x = "//div[@class='inventory_list']/div[@class='inventory_item']["
        z = "]//button[text()='ADD TO CART']"
       #print("abc" + str(index))
        #print(x + str(index) + z)
        return (By.XPATH, (x + str(index) + z))

    def REMOVE_TO_CART_BUTTON(index):
        x = "//div[@class='inventory_list']/div[@class='inventory_item']["
        z = "]//button[text()='REMOVE']"
        return (By.XPATH, (x + str(index) + z))

class CartLocators(object):
    CHECK_OUT = (By.XPATH, "//*[@class='btn_action checkout_button']")
    CONTINUTE_BUTTON_SHOPPING = (By.XPATH, "//*[@class='btn_secondary']")

    def REMOVE_TO_CART_BUTTON(index):
        x = "//div[@class='cart_list']//div[@class='cart_item']["
        z = "]//button[text()='REMOVE']"
        return (By.XPATH, (x + str(index) + z))

class CheckoutStepOneLocators(object):
    INPUT_FIRSTNAME = (By.ID, 'first-name')
    INPUT_LASTNAME = (By.ID, 'last-name')
    INPUT_ZIPCODE = (By.ID, 'postal-code')
    CANCEL_BUTTON_1 = (By.XPATH, "//div[@class='checkout_buttons']/a[text()='CANCEL']")
    CONTINUTE_BUTTON = (By.XPATH, "//*[@class='btn_primary cart_button']")



class CheckoutStepTwoLocators(object):
    CANCEL_BUTTON_2 = (By.XPATH, "//div[@class='cart_footer']/a[text()='CANCEL']")
    FINISH_BUTTON = (By.XPATH, "//*[@class='btn_action cart_button']")

class CheckoutComplete(object):
    pass