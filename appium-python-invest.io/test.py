#android_calculator_appium.py. Run these test cases on Android 4.2
import unittest
import time
import config
import HtmlTestRunner


#using Unit Test
class AndroidInvestorAITest(unittest.TestCase):
	
	def setUp(self):
		config.initial_set()

	# test case to test addition operation
	def test_verify_landing_page(self):
		config.wait_explicit(10, config.get_property('FIRST_TIME_USER'))
		assert config.find_element(config.get_property('FIRST_TIME_USER')).is_displayed() == True

	def test_verify_login(self):
		assert config.login()  == True
	

	def test_verify_stock_search_operation(self):
		config.login()
		config.skip_terms() 	
		config.find_element(config.get_property('SEARCH_STOCK_FIELD')).set_value("tata")
		config.key_press(10)
		config.key_press(67)
		config.wait_explicit(10, config.get_property('VIEW_COMPANY_NAME'))
		config.find_element(config.get_property('SEARCH_COMPANY_NAME_LINK')).click()
		assert float(config.find_element(config.get_property('STOCK_PRICE')).text) > 900


	def tearDown(self):
		config.tearDown()
		
html_report_dir = './html_report'		
if __name__ == "__main__":
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))
