from selenium import webdriver
import unittest


class VisitingTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:63342/PycharmProjects/my_cv_site/home.html')
        self.driver.implicitly_wait(3)

    def test_run_menu_page_check_title_n_contents_back_to_home(self):
        pages = ['O mnie', 'Wykształcenie', 'Systemy', 'Programowanie', 'Kontakt']
        for p in pages:
            page = self.driver.find_element_by_class_name('menu').find_element_by_partial_link_text(p)
            page.click()
            self.assertIn(p, self.driver.title)

            contents = self.driver.find_element_by_id('contents').text
            self.assertIn(p, contents)

            back = self.driver.find_element_by_id('logo')
            back.click()
            self.assertIn('Aleksandra', self.driver.title)

    def test_run_english_page_check_title_n_contents_back_to_home(self):
        english = self.driver.find_element_by_partial_link_text('english')
        english.click()

        pages = ['About me', 'Education', 'Systems', 'Web', 'Contact']
        for p in pages:
            page = self.driver.find_element_by_class_name('menu').find_element_by_partial_link_text(p)
            page.click()
            self.assertIn(p, self.driver.title)

            contents = self.driver.find_element_by_id('contents').text
            self.assertIn(p, contents)

            back = self.driver.find_element_by_id('logo')
            back.click()
            self.assertIn('Aleksandra', self.driver.title)

    def test_run_page_run_english_check_titles(self):
        pages = ['O mnie', 'Wykształcenie', 'Systemy', 'Programowanie', 'Kontakt']
        index = 0
        for p in pages:
            page = self.driver.find_element_by_class_name('menu').find_element_by_partial_link_text(p)
            page.click()
            self.assertIn(p, self.driver.title)

            english = self.driver.find_element_by_partial_link_text('english')
            english.click()

            title = self.driver.title
            english_titles = ['About me', 'Education', 'Systems', 'Web', 'Contact']
            self.assertIn(english_titles[index], title)

            polish = self.driver.find_element_by_partial_link_text('polski')
            polish.click()
            index += 1

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

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
