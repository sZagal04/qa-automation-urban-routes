from selenium.common import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait

import data
import json
import time

from selenium import webdriver

import helpers as helpers
from pages import UrbanRoutesPage




class TestUrbanRoutes:

    def setup_class(self):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        self.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_verify_tarifa_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_request_taxy()
        routes_page.select_comfort()
        assert 'active' in routes_page.get_comform_selected_class()

    def test_fill_phone_number(self):
        page = UrbanRoutesPage(self.driver)
        page.set_phone(data.phone_number)
        assert page.get_phone_number() == data.phone_number

    def test_add_credit_card(self):
        page = UrbanRoutesPage(self.driver)
        page.add_credit_card(data.card_number, data.card_code)
        assert page.get_card() == "Tarjeta"

    def test_set_message(self):
        page = UrbanRoutesPage(self.driver)
        page.set_message(data.message_for_driver)
        assert page.get_comment() == data.message_for_driver

    def test_request_blanket_and_tissues(self):
        page = UrbanRoutesPage(self.driver)
        page.request_blanket_and_tissues()
        assert page.get_blanket()
        assert page.get_tissues()

    def test_add_icecreams(self):
        page = UrbanRoutesPage(self.driver)
        page.add_icecreams(2)
        assert page.get_icecreams() == "2"

    def test_order_taxies(self):
        page = UrbanRoutesPage(self.driver)
        page.order_taxi()
        assert page.return_search_modal()

    def test_wait_for_search_moadal(self):
        page = UrbanRoutesPage(self.driver)
        page.wait_for_search_modal()
        page.wait_for_driver_info()
        assert page.return_driver_info()

    def teardown_class(self):
        self.driver.quit()
