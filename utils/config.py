#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

"""Environment Configuration Class"""

from utils.get_args_from_cli import get_args


class Config:
	"""
	Environment Configuration Class

	Source:
	https://www.udemy.com/elegant-automation-frameworks-with-python-and-pytest
	"""

	def __init__(self):
		params = get_args()

		self.__base_url = {
			'google': 'https://www.google.com/',
			'BotDetectCaptcha': 'https://captcha.com/',
			'integration': '',
			'production': '',
			'localhost': 'http://localhost:8080',
		}[params['env'].lower()]

		self.__is_headless = params['is_headless']

		self.__browser = {
			'chrome': 'chrome',
			'edge': 'edge',
			'firefox': 'mozilla'
		}[params['browser'].lower()]

		self.__print_run_config()

	@property
	def browser(self):
		return self.__browser

	@property
	def base_url(self):
		return self.__base_url

	@property
	def is_headless(self):
		return self.__is_headless

	def __print_run_config(self):
		"""
		Prints run configurations
		:return:
		"""
		print('\nRun configurations -> Browser: {}\n'
		      'Run configurations -> Environment: {}\n'
		      'Run configurations -> Is Headless: {}'.format(self.browser, self.base_url, self.is_headless))
