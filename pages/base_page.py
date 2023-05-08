from selenium.webdriver.common.by import By


class BasePage:
    sign_in = (By.CSS_SELECTOR, '.user-li a')
    guide_link = (By.CSS_SELECTOR, '.desktop a[href*="guide"]')

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def open_page(self):
        self.driver.get(self.link)

    def click_header_link(self, link_name):
        if link_name == 'sign in':
            self.driver.find_element(*self.sign_in).click()
        if link_name == 'guide':
            self.driver.find_element(*self.guide_link).click()



