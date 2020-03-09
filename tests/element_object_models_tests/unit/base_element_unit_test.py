#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest

from page_locators.base_page_locator import BasePageLocator
from tests.config import Config
from utils.driver import Driver

from element_object_models.base_element import BaseElement


class BaseElementUnitTestCase(unittest.TestCase):

	def test_base_el_not_null(self):

		config = Config()

		driver = Driver(config=config,
		                is_debug=True).get_driver()

		locator = BasePageLocator().LOGO

		element = BaseElement(driver=driver,
		                      explicit_wait_time=10,
		                      locator=locator).element

		self.assertIsNotNone(element)
