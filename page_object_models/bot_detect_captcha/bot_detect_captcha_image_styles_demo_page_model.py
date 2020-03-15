#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.config import Config
from utils.driver import Driver
from page_object_models.bot_detect_captcha.bot_detect_captcha_base_page_model import BotDetectCaptchaBasePageModel
from expected_results.page_content.bot_detect_captcha_content.bot_detect_captcha_image_styles_demo_content import \
	BotDetectCaptchaImageStylesDemoPageContent


class BotDetectCaptchaImageStylesDemo(BotDetectCaptchaBasePageModel):
	def __init__(self,
	             config: Config,
	             driver: Driver,
	             explicit_wait_time: int,
	             implicit_wait_time: int = 0):

		super().__init__(config,
		                 driver,
		                 explicit_wait_time,
		                 implicit_wait_time)

		self.__url = BotDetectCaptchaImageStylesDemoPageContent.URL

	@property
	def url(self) -> str:
		"""
		Returns BotDetect Captcha Image Styles Demo web page URL
		:return:
		"""
		return self.__url

	def go(self) -> None:
		"""
		Opens test web page
		:return:
		"""
		self.driver.get(self.base_url + self.url)
		self.driver.maximize_window()
		return None
