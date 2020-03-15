#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By


class BotDetectCaptchaBasePageLocator:
	"""
	Holds all relevant locators for any BotDetect Captcha page web elements.
	Each locator is a tuple.
	
	Separate the locator strings from the place where they are being used.
	"""

	# Website logo
	LOGO = (By.XPATH, "//*[@id=\"top\"]/div[2]/div[2]/div/div[1]/a/span")
