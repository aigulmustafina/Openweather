import os
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MarketplacePage(BasePage):
    history_bulk_search_import = (By.XPATH, "//button[contains(text(), 'Import')]")
    button_import_csv = (By.XPATH, "//button[contains(text(), 'Import CSV file')]")
    input_field_upload_file = (By.ID, "importCSV")
    div_field_upload_file = (By.XPATH, "//*[@id='app']/div[2]/div")
    location_name_table = (By.XPATH, "//table[@class='material-table']/tbody/tr/td[2]")
    latitude_table = (By.XPATH, "//table[@class='material-table']/tbody/tr/td[3]")
    longitude_table = (By.XPATH, "//table[@class='material-table']/tbody/tr/td[4]")
    history_bulk_title = (By.XPATH, "//h5/a[contains(text(), 'History Bulk')]")

    def check_csv_file(self):
        csv_file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'test_data/test_search_by_import.csv'))
        f = open(csv_file_path, 'r')
        try:
            csv_str = f.readline()
        finally:
            f.close()
        expected_location, expected_latitude, expected_longitude = csv_str.split(";")

        self.driver.find_element(*self.history_bulk_title).click()

        input_file = self.driver.find_element(*self.input_field_upload_file)
        div_input_file = self.driver.find_element(*self.div_field_upload_file)

        self.driver.execute_script("arguments[0].setAttribute('class','visible')", input_file)
        self.driver.execute_script("arguments[0].setAttribute('class','visible')", div_input_file)

        input_file.send_keys(csv_file_path)

        actual_location = self.driver.find_element(*self.location_name_table)
        actual_latitude = self.driver.find_element(*self.latitude_table)
        actual_longitude = self.driver.find_element(*self.longitude_table)
        assert actual_location.text.strip() == expected_location \
               and actual_latitude.text.strip() == expected_latitude \
               and actual_longitude.text.strip() == expected_longitude

