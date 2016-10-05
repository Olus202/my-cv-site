from selenium import webdriver
import unittest

class VisitingTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_run_home_page_and_check_title(self):
        self.browser.get('http://localhost:63342/PycharmProjects/my_cv_site/home.html')

        self.assertIn('Aleksandra Bacik-Polus', self.browser.title)

    def test_end(self):
        self.fail('End of test')

if __name__ == '__main__':
    unittest.main()