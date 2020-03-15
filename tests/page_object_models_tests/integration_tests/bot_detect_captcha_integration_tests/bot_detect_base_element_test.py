#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest
from tests.config import Config
from utils.driver import Driver
from page_object_models.bot_detect_captcha.bot_detect_captcha_image_styles_demo_page_model import \
	BotDetectCaptchaImageStylesDemo


class BaseElementIntegrationTestCase(unittest.TestCase):

	def test_bot_detect_captcha_image_styles_demo_page_logo(self):

		config = Config()

		driver = Driver(config=config, is_debug=True).get_driver()

		page = BotDetectCaptchaImageStylesDemo(config=config,
		                                       driver=driver,
		                                       explicit_wait_time=30,
		                                       implicit_wait_time=5)

		page.go()

		element = page.logo

		self.assertIsNotNone(element)

		page.close()
