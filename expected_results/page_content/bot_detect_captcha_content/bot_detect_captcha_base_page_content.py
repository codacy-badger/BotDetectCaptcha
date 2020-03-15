#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/
from tests.config import Config


class BotDetectCaptchaBasePageContent:
	"""
	Holds expected context values for any
	BotDetect Captcha relevant page items
	"""

	URL = ''

	TITLE = 'BotDetect CAPTCHA Generator'

	BOT_DETECT_LOGO = {
		'href': "./",
		'title': "BotDetect CAPTCHA Homepage",
		'class': "logo"
	}
