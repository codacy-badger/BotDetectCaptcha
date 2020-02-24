#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator


class CaptchaDemoLocator(BasePageLocator):
	"""
	Holds all relevant locators for BotDetect CAPTCHA Demo page web elements.
	Each locator is a tuple.

	Separate the locator strings from the place where they are being used.
	"""

	# Page header
	HEADER = (By.XPATH, "//*[@id=\"main\"]/h1")

	# Captcha Image
	CAPTCHA_IMG = (By.XPATH, "//*[@id=\"c_captchademo_samplecaptcha_CaptchaImage\"]")

	# Reload Captcha Button
	RELOAD_CAPTCHA_BTN = (By.XPATH, "//*[@id=\"c_captchademo_samplecaptcha_ReloadIcon\"]")

	# Sound Button
	SOUND_BTN = (By.XPATH, "//*[@id=\"c_captchademo_samplecaptcha_SoundIcon\"]")

	# Input field
	INPUT_FIELD = (By.XPATH, "//*[@id=\"CaptchaCodeTextBox\"]")

	# Validate Button
	VALIDATE_BTN = (By.XPATH, "//*[@id=\"ValidateCaptchaButton\"]")

	# Locale Combo Box
	LOCALE_COMBO = (By.XPATH, "//*[@id=\"LocaleDropDown\"]")

	# Code Length Combo Box
	CODE_LENGTH_COMBO = (By.XPATH, "//*[@id=\"CodeLengthDropDown\"]")

	# Code Style Combo Box
	CODE_STYLE_COMBO = (By.XPATH, "//*[@id=\"CodeStyleDropDown\"]")

	# Custom Light Color Combo Box
	CUSTOM_LIGHT_COLOR_COMBO = (By.XPATH, "//*[@id=\"CustomLightColorDropDown\"]")

	# Custom Dark Color Combo Box
	CUSTOM_DARK_COLOR_COMBO = (By.XPATH, "//*[@id=\"CustomDarkColorDropDown\"]")

	# Image Format Combo Box
	IMAGE_FORMAT_COMBO = (By.XPATH, "//*[@id=\"ImageFormatDropDown\"]")

	# Sound Format Combo Box
	SOUND_FORMAT_COMBO = (By.XPATH, "//*[@id=\"SoundFormatDropDown\"]")

	# Image Width Input
	IMAGE_WIDTH_INPUT = (By.XPATH, "//*[@id=\"WidthTextBox\"]")

	# Image Height Input
	IMAGE_HEIGHT_INPUT = (By.XPATH, "//*[@id=\"HeightTextBox\"]")
