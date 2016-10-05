from selenium import webdriver
import unittest
import time

class VisitingTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.base = 'http://localhost:63342/PycharmProjects/my_cv_site/'
        self.browser.get(self.base + 'home.html')
        self.browser.implicitly_wait(3)


    def tearDown(self):
        self.browser.quit()

    def test_run_home_page_and_check_title(self):
        self.browser.get(self.base + 'home.html')

        self.assertIn('Witam', self.browser.title)

    def test_run_menu_pages(self):
        pages = ['O mnie', 'Wykształcenie', 'Systemy', 'Programowanie', 'Kontakt']
        for p in pages:
            link = self.browser.find_element_by_class_name('menu').find_element_by_partial_link_text(p)
            link.click()

            self.assertIn(p, self.browser.title)
            time.sleep(3)

    def test_end(self):
        self.fail('End of test')

if __name__ == '__main__':
    unittest.main()