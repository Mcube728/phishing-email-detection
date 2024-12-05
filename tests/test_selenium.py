import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

    def test_url_prediction(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")  # Adjust if necessary

        # Find the input field and button
        url_input = driver.find_element(By.ID, "urlInput")
        submit_button = driver.find_element(By.ID, "submitBtn")

        # Input a URL and submit the form
        test_url = "https://youtube.com"
        url_input.send_keys(test_url)
        submit_button.click()

        # Use WebDriverWait to wait for the result div to contain the expected text
        try:
            result_div = WebDriverWait(driver, 60).until(
                EC.text_to_be_present_in_element((By.ID, "result"), "Results:")
            )
            self.assertIn("Results:", driver.find_element(By.ID, "result").text)
            self.assertIn(test_url, driver.find_element(By.ID, "result").text)
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

