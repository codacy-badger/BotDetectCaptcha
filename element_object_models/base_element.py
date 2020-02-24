"""Base Element Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import selenium.webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, \
    NoSuchElementException, \
    NoSuchAttributeException


class BaseElement:
    """
    Base Web Element
    """

    def __init__(self, driver: selenium.webdriver, explicit_wait_time: int, locator=None):
        self.__driver = self.__set_driver(driver)
        self.__explicit_wait_time = explicit_wait_time
        self.__locator = self.__set_locator(locator)
        self.__element = self.__find_element()

    @property
    def explicit_wait_time(self):
        """
        Returns Explicit wait time
        :return:
        """
        return self.__explicit_wait_time

    @property
    def driver(self):
        """
        Returns selenium.webdriver object
        :return:
        """
        return self.__driver

    def attribute(self, attribute: str):
        """
        Returns attribute value
        :return:
        """
        try:
            atr = self.element.get_attribute(attribute)
            # print('\nattribute: {}, object: {}'.format(attribute, atr))  # debug only
            return atr

        except TimeoutException:
            raise NoSuchAttributeException(
                '\nERROR: The element has no attribute "{}".\n'
                'LOCATOR: {}\n'.format(attribute, self.locator))

    @property
    def element(self):
        """
        Returns Element instance
        :return:
        """
        return self.__element

    @property
    def locator(self):
        """
        Returns locator object (tuple)
        :return:
        """
        return self.__locator

    def __find_element(self):
        """
        Returns web element or NoSuchElementException in
        case element does not exist on the DOM
        :return:
        """
        try:
            element = WebDriverWait(self.driver, self.explicit_wait_time).until(
                EC.presence_of_element_located(self.locator))
            return element

        except TimeoutException:
            raise NoSuchElementException(
                '\nERROR: can not find element. The element is not present on the DOM.\n'
                'LOCATOR: {}\n'.format(self.locator))

    @staticmethod
    def __set_driver(driver: selenium.webdriver):
        """
        Check if driver of type: selenium.webdriver
        :param driver:
        :return:
        """
        BaseElement.__check_driver_type(driver)
        return driver

    @staticmethod
    def __check_driver_type(driver):

        # print('\nDRIVER TYPE: {}, {}\n'.format(type(driver),
        # driver.capabilities['browserName']))  # Debug only
        if driver.capabilities['browserName'] == 'chrome':
            if not isinstance(driver, selenium.webdriver.chrome.webdriver.WebDriver):
                raise TypeError('\nERROR: driver must be of type '
                                '"selenium.webdriver.chrome_tests.webdriver.WebDriver"\n')
            return None

        if driver.capabilities['browserName'] == 'firefox':
            if not isinstance(driver, selenium.webdriver.firefox.webdriver.WebDriver):
                raise TypeError('\nERROR: driver must be of type '
                                '"selenium.webdriver.firefox.webdriver.WebDriver"\n')
            return None

        if driver.capabilities['browserName'] == 'MicrosoftEdge':
            if not isinstance(driver, selenium.webdriver.edge.webdriver.WebDriver):
                raise TypeError('\nERROR: driver must be of type '
                                '"selenium.webdriver.edge.webdriver.WebDriver"\n')
            return None

        raise TypeError('\nERROR: unsupported webdriver type: '
                        '{}. Browser: {}\n'.format(type(driver),
                                                   driver.capabilities['browserName']))

    @staticmethod
    def __set_locator(locator: tuple):
        """
        Check if locator of type: tuple
        :param locator:
        :return:
        """
        if not isinstance(locator, tuple):
            raise TypeError('\nERROR: locator must be of type TUPLE\n')
        return locator
