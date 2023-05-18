import pytest
from pages.main_page import MainPage
from test_data.main_page_data import main_page_data

URL = 'https://openweathermap.org/'

def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url

def test_tc_000_00_01_verify_sign_in_link_redirects_to_valid_page(driver, open_and_load_main_page):
    page = MainPage(driver)
    page.check_header_link_opens_page('sign')

@pytest.mark.parametrize('city', main_page_data["cityNames"])
def test_tc_000_00_02_verify_requested_city_displayed_for_valid_input(driver, open_and_load_main_page, wait, city):
    page = MainPage(driver)
    page.check_city_searching_result(wait, city)

def test_tc_000_00_03_verify_no_results_displayed_for_invalid_input(driver, open_and_load_main_page, wait):
    page = MainPage(driver)
    page.check_city_searching_result(wait, 'Neverland')


def test_verify_all_search_options_contain_valid_city(driver, open_and_load_main_page, wait):
    page = MainPage(driver)
    page.check_dropdown_options('Tokyo')
