import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("phones")
        self.search_field.submit()

        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(2, len(products))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
