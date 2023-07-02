import unittest
from selenium import webdriver

class WebsiteLoadingTest(unittest.TestCase):
    def setUp(self):
        # Set up the Selenium webdriver
        self.driver = webdriver.Firefox()
    
    def test_website_loading(self):
        # Load the atg.world website
        self.driver.get("https://www.atg.world")

        # Verify if the website title is correct
        expected_title = "ATG - Explore a new reality"
        actual_title = self.driver.title
        self.assertEqual(actual_title, expected_title)

    def tearDown(self):
        # Quit the Selenium webdriver
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

