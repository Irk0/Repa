# from .base_page import BasePage
# from .locators import MainPageLocators
# from .login_page import LoginPage
# from selenium.webdriver.common.by import By
# class MainPage(BasePage):
#     def go_to_login_page(self):
#         login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#         login_link.click()
#         alert = self.browser.switch_to.alert
#         alert.accept()
#         return LoginPage(browser=self.browser, url=self.browser.current_url)
#
#
#     # def should_be_login_link(self):
#     #     self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
#
#     def should_be_login_link(self):
#         assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
#


from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)