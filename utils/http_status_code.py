#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import requests


def get_http_status_code(url: str) -> None:
	"""
	Returns HTTP status code
	Using requests library
	:param url:
	:return:
	"""

	try:
		response = requests.get(url)
		print("\nURL: {}\nHTTP Status code: {}".format(url, response.status_code))
	except ConnectionError as er:
		print('\n{}\n'.format(er))
	return None
