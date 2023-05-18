from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
    search_dropdown = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
    search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
    search_city_field = (By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_button = (By.CSS_SELECTOR, "button[class ='button-round dark']")
    displayed_city = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
    sign_in_link = (By.CSS_SELECTOR, '.user-li a')
    no_results_notification = (By.CSS_SELECTOR, 'div.widget-notification > span')
    not_found_message = (By.CSS_SELECTOR, '.sub.not-found.notFoundOpen')

    def fill_search_city_field(self, city):
        search_city_input = self.driver.find_element(*self.search_city_field)
        search_city_input.send_keys(city)

    def click_search_city_button(self, city):
        self.fill_search_city_field(city)
        self.driver.find_element(*self.search_button).click()

    def check_dropdown_options(self, city):
        self.click_search_city_button(city)
        options = self.driver.find_elements(*self.search_dropdown)
        for option in options:
            assert city in option


    def check_city_searching_result(self, wait, city):
        self.click_search_city_button(city)
        expected_city = city
        expected_error_message = f'No results for {city}'
        if self.element_is_displayed(*self.no_results_notification, wait):
            error_message = wait.until(EC.visibility_of_element_located(self.no_results_notification))
            actual_error_message = error_message.text
            assert expected_error_message == actual_error_message
        else:
            wait.until(EC.element_to_be_clickable(self.search_dropdown_option)).click()
            wait.until(EC.text_to_be_present_in_element(self.displayed_city, city))
            actual_city = self.driver.find_element(*self.displayed_city).text
            assert expected_city in actual_city

    # def search_with_invalid_value(self, wait, value):
    #     search_city_input = self.driver.find_element(*self.search_city_field)
    #     search_city_input.send_keys(value)
    #     self.driver.find_element(*self.search_button).click()
    #     expected_error_message = f'No results for {value}'
    #     error_message = wait.until(EC.visibility_of_element_located(self.no_results_notification))
    #     actual_error_message = error_message.text
    #     assert expected_error_message == actual_error_message

