from pages.marketplace_page import MarketplacePage

URL = 'https://home.openweathermap.org/marketplace'


def test_TC_007_02_04_verify_search_by_import_csv(driver, wait):
    page = MarketplacePage(driver, link=URL)
    page.open_page()
    page.check_csv_file()