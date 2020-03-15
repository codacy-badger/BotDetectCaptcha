#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.config import Config
from utils.driver import Driver


class BasePageModel:
	"""
	The page object pattern intends creating
	an object for each web page.

	By following this technique a layer of separation
	between the test code and technical implementation is created.
	"""

	def __init__(self,
	             config: Config,
	             driver: Driver,
	             explicit_wait_time: int,
	             implicit_wait_time: int = 0):

		self.__config = config
		self.__implicit_wait_time = implicit_wait_time
		self.__explicit_wait_time = self.__set_explicit_wait(explicit_wait_time)
		self.__driver = self.__set_driver(driver)
		self.__set_implicit_wait(implicit_wait_time)

	@property
	def config(self) -> Config:
		"""
		Returns current configurations:
			base_url
			browser
			is_headless
		:return:
		"""
		return self.__config

	@property
	def implicit_wait_time(self) -> int:
		"""
		Returns Implicit Wait Time

		Implicit waits are used to provide a default waiting
		time (say 30 seconds) between each consecutive test
		step/command across the entire test script. Thus, the
		subsequent test step would only execute when the 30
		seconds have elapsed after executing the previous test
		step/command.

		Being easy and simple to apply, implicit wait introduces
		a few drawbacks as well. It gives rise to the test script
		execution time as each of the commands would be ceased to
		wait for a stipulated amount of time before resuming the
		execution.

		Source:
		https://www.softwaretestinghelp.com/
		selenium-webdriver-waits-selenium-tutorial-15/
		:return:
		"""
		return self.__implicit_wait_time

	@property
	def explicit_wait_time(self) -> int:
		"""
		Returns Explicit Wait Time

		Explicit waits are used to halt the execution until the time
		a particular condition is met or the maximum time has elapsed.
		Unlike Implicit waits, Explicit waits are applied for a
		particular instance only.

		Source:
		https://www.softwaretestinghelp.com/
		selenium-webdriver-waits-selenium-tutorial-15/
		:return:
		"""
		return self.__explicit_wait_time

	@staticmethod
	def __set_driver(driver):
		"""
		Check if driver of type: selenium.webdriver
		:param driver:
		:return:
		"""

		# print('\nDriver type: {}'.format(type(driver)))  # debug only
		if isinstance(driver, Driver):
			return driver.get_driver()

		return driver

	def __set_implicit_wait(self, implicit_wait_time: int) -> None:
		"""
		The default value of time that can be set using Implicit wait is zero.
		Its unit is in seconds.

		Implicit wait remains associated with the web element until it gets destroyed.
		:param implicit_wait_time:
		:return:
		"""
		if type(implicit_wait_time) != int:
			raise TypeError('\nERROR: wrong data type. '
			                'Please set "implicit_wait_time" value as integer.\n')
		self.__driver.implicitly_wait(implicit_wait_time)
		return None

	@staticmethod
	def __set_explicit_wait(explicit_wait_time: int) -> int:
		"""
		The default value of explicit wait time.
		Its unit is in seconds.
		:param explicit_wait_time:
		:return:
		"""
		if type(explicit_wait_time) != int:
			raise TypeError('\nERROR: wrong data type. '
			                'Please set "explicit_wait_time" value as integer.\n')
		return explicit_wait_time

	def quit(self) -> None:
		"""
		Close web browser window (including all opened tabs)
		:return:
		"""
		if self.__driver:
			self.__driver.quit()
		return None

	def close(self) -> None:
		"""
		Close current tab
		:return:
		"""
		if self.__driver:
			self.__driver.close()
		return None

	@property
	def driver(self):
		"""
		Returns Selenium webdriver object
		:return:
		"""
		return self.__driver

	@property
	def title(self) -> str:
		"""
		Returns web page title
		:return:
		"""
		title: str = self.__driver.title
		return title

	@property
	def url(self) -> str:
		"""
		Returns current URL
		:return:
		"""
		url: str = self.__driver.current_url
		return url
