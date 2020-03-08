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

		self._base_url = {
			'google': 'https://www.google.com/',
			'integration': '',
			'production': '',
			'localhost': 'http://localhost:8080',
		}[params['env'].lower()]

	@property
	def base_url(self):
		return self._base_url
