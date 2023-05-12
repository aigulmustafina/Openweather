from selenium.webdriver.common.by import By
URL = 'https://openweathermap.org/'
from pages.main_page import MainPage


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url

def test_open_sign_in_link(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.click_header_link('sign in')
    assert 'sign' in driver.current_url

def test_should_display_value_for_valid_input(driver, open_and_load_main_page, wait):
    page = MainPage(driver)
    page.search_city(wait, 'New York')

def test_should_display_not_found_for_invalid_input(driver, open_and_load_main_page, wait):
    page = MainPage(driver)
    page.search_city(wait, 'Neverland')
