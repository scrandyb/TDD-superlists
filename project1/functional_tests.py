from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Bob wants to go to that cool to-do app. So he goes to the homepage
		self.browser.get('http://localhost:8000')

		# He notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# He is invited to enter a to-do item right away

		# He types "Cook bacon" into a text box

		# When he hits enter, the page updates, and now the page lists
		# "1: Cook bacon" as an item in a to-do list

		# There is still a text box inviting her to add another item. 
		# He adds "Eat the bacon"

		# The page updates again, and shows him both items in the list

		# Bob wonders whether the site will remember the list. Then he sees
		# that the site has generated a unique URL for him -- there is some
		# explanatory text to that effect

		# Bob visits that URL - his to-do list is still there

		# Satisfied, Bob closes his browser, full of bacon
		
if __name__ == '__main__':
	unittest.main()

	