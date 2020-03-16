#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest
import allure
from tests.config import Config
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from page_object_models.bot_detect_captcha.bot_detect_captcha_image_styles_demo_page_model import \
	BotDetectCaptchaImageStylesDemoModel
from expected_results.page_content.bot_detect_captcha_content.bot_detect_captcha_image_styles_demo_content import \
	BotDetectCaptchaImageStylesDemoPageContent
from utils.step_definition import step_definition


@allure.epic('BotDetect CAPTCHA')
@allure.parent_suite('Unit')
@allure.suite("BotDetect Captcha")
@allure.sub_suite('Positive Tests')
@allure.feature("BotDetect CAPTCHA Demo - Image Styles Page")
@allure.story('Base Page Elements Verification')
@allure.tag('LOGO', 'URL', 'BotDetect CAPTCHA Demo - Image Styles')
@allure.link(url='https://captcha.com/demos/image-styles/captcha-demo.aspx',
             name='BotDetect CAPTCHA Demo - Image Styles')
@screenshot_on_fail()
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
		allure.dynamic.description("""
			Forgot Login Info test case:
			1. Open 'BotDetect CAPTCHA Demo - Image Styles' web page
			2. Verify web page logo is not null
			3. Close web browser
		""")
		allure.dynamic.title("'BotDetect CAPTCHA Demo - Image Styles' > Logo")
		allure.dynamic.severity(allure.severity_level.TRIVIAL)

		step_definition(self,
		                expected=True,
		                actual=bool(self.page.logo),
		                act=None,
		                step_description="Assert that page logo object is not null",
		                click=False)

	def test_bot_detect_captcha_image_styles_demo_url(self):
		allure.dynamic.description("""
			Forgot Login Info test case:
			1. Open 'BotDetect CAPTCHA Demo - Image Styles' web page
			2. Verify web page URL
			3. Close web browser
		""")
		allure.dynamic.title("'BotDetect CAPTCHA Demo - Image Styles' > URL")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		step_definition(self,
		                expected=self.config.base_url + BotDetectCaptchaImageStylesDemoPageContent.URL,
		                actual=self.page.url,
		                act=None,
		                step_description="Assert web page URL",
		                click=False)

	def test_bot_detect_captcha_image_styles_demo_title(self):
		allure.dynamic.description("""
			Forgot Login Info test case:
			1. Open 'BotDetect CAPTCHA Demo - Image Styles' web page
			2. Verify web page title
			3. Close web browser
		""")
		allure.dynamic.title("'BotDetect CAPTCHA Demo - Image Styles' > Title")
		allure.dynamic.severity(allure.severity_level.MINOR)

		step_definition(self,
		                expected=BotDetectCaptchaImageStylesDemoPageContent.TITLE,
		                actual=self.page.title,
		                act=None,
		                step_description="Assert web page title",
		                click=False)
