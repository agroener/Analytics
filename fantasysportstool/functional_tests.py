from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_a_new_account_or_login(self):
        # Bob has heard about a cool new online basketball fantasy web-tool.
        # He goes to check out its homepage.
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention 'basketball'
        self.assertIn('basketball',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('basketball', header_text)

        # He is invited to make an account straight-away (or sign in
        # to an existing account).
        inputbox = self.browser.find_element_by_id('id_username')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your username'
        )

        # He types his email address (or username) and password
        inputbox.send_keys('BobBelcher1975')

        # When he hits enter, the pages updates with a request for his password
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_password')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == "BobBelcher1975" for row in rows),
            "Username did not appear in inputbox"
        )

        # While he is entering his credentials, he notices today's
        # predictions regarding which players are expected to outperform
        # their long-term fantasy point averages.

        self.fail('Finish the test!')

if __name__ == "__main__":
    unittest.main(warnings='ignore')
