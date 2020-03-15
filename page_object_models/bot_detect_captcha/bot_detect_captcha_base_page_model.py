#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.config import Config
from utils.driver import Driver
from element_object_models.base_element import BaseElement
from page_object_models.base_page_model import BasePageModel
from page_locators.bot_detect_captcha_locators.bot_detect_captcha_base_page_locator import \
	BotDetectCaptchaBasePageLocator
from expected_results.page_content.bot_detect_captcha_content.bot_detect_captcha_base_page_content import \
	BotDetectCaptchaBasePageContent


class BotDetectCaptchaBasePageModel(BasePageModel):
	"""
	The BotDetect Captcha Base Page object pattern intends
	creating an object for each web page.
	"""

	def __init__(self,
	             config: Config,
	             driver: Driver,
	             explicit_wait_time: int,
	             implicit_wait_time: int = 0):

		super().__init__(config,
		                 driver,
		                 explicit_wait_time,
		                 implicit_wait_time)

		self.__base_url = config.base_url + BotDetectCaptchaBasePageContent.URL

	@property
	def base_url(self):
		"""
		Returns base URL
		:return:
		"""
		return self.__base_url

	def go(self) -> None:
		"""
		Opens test web page
		:return:
		"""
		self.driver.get(self.base_url)
		self.driver.maximize_window()
		return None

	@property
	def logo(self):
		return BaseElement(driver=self.driver,
		                   explicit_wait_time=self.explicit_wait_time,
		                   locator=BotDetectCaptchaBasePageLocator.LOGO)
