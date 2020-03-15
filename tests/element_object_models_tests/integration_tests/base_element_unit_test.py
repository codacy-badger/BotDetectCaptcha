#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest
from tests.config import Config
from utils.driver import Driver
from page_object_models.base_page_model import BasePageModel


class BaseElementUnitTestCase(unittest.TestCase):

	def test_base_el_not_null(self):

		config = Config()

		driver = Driver(config=config, is_debug=True).get_driver()

		page = BasePageModel(config=config,
		                     driver=driver,
		                     explicit_wait_time=30,
		                     implicit_wait_time=5)

		page.go()

		element = page.logo

		self.assertIsNotNone(element)

		page.close()
