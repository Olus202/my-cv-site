from selenium import webdriver
import unittest


class VisitingTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:63342/PycharmProjects/my_cv_site/home.html')
#        self.driver.implicitly_wait(10)

    def test_run_home_page_and_check_title(self):
        self.assertIn('Witam', self.driver.title)

    def test_run_menu_pages(self):
        pages = ['O mnie', 'Wykształcenie', 'Systemy', 'Programowanie', 'Kontakt']
        for p in pages:
            link = self.driver.find_element_by_class_name('menu').find_element_by_partial_link_text(p)
            link.click()

            self.assertIn(p, self.driver.title)

    def test_run_linkedin_link(self):
        link = self.driver.find_element_by_class_name("icon-linkedin-circled")
        link.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertIn("LinkedIn", self.driver.title)

    def test_run_github_link(self):
        link = self.driver.find_element_by_class_name("icon-github-circled")
        link.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertIn("GitHub", self.driver.title)

    def test_run_blog_link(self):
        link = self.driver.find_element_by_class_name("icon-newspaper")
        link.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertIn("poza drzwiami", self.driver.title)

    def test_end(self):
        self.fail('End of test')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
