#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest
import allure
from tests.config import Config
from page_object_models.bot_detect_captcha.bot_detect_captcha_image_styles_demo_page_model import \
	BotDetectCaptchaImageStylesDemoModel
from expected_results.page_content.bot_detect_captcha_content.bot_detect_captcha_image_styles_demo_content import \
	BotDetectCaptchaImageStylesDemoPageContent
from utils.open_web_browser import open_web_browser


class BaseElementUnitTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Set up initial configs"):
			cls.page = None
			cls.config = Config()

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close Web Browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def setUp(self):
		with allure.step("Initial data setup: {}".format(BotDetectCaptchaImageStylesDemoPageContent.URL)):
			self.page_model = BotDetectCaptchaImageStylesDemoModel
			self.page_context = BotDetectCaptchaImageStylesDemoPageContent
			with allure.step("Open web browser"):
				self.page = open_web_browser(config=self.config,
				                             page_model=self.page_model,
				                             page_content=self.page_context)

	def tearDown(self):
		with allure.step("Close current tab"):
			if self.page:
				self.page.close()

	def test_bot_detect_captcha_image_styles_demo_logo(self):
		with allure.step("Assert that page logo object is not null"):
			logo = self.page.logo
			self.assertIsNotNone(logo)

	def test_bot_detect_captcha_image_styles_demo_url(self):
		with allure.step("Assert web page URL"):
			url = self.page.url
			expected = self.config.base_url + BotDetectCaptchaImageStylesDemoPageContent.URL
			self.assertEqual(expected, url)

