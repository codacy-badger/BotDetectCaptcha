#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By


class BasePageLocator:
	"""
	Holds all relevant locators for any page web elements.
	Each locator is a tuple.
	
	Separate the locator strings from the place where they are being used.
	"""

	# Website logo
	LOGO = (By.XPATH, "//*[@id=\"top\"]/div[1]/div[2]/div/div[1]/a/span")

	# Captcha Demo menu item
	CAPTCHA_DEMO_MENU_ITEM = (By.XPATH, "//*[@id=\"left\"]/div[1]/ul/li[1]/ul/li[3]/a")

