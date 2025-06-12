import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_comfort_plan()

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_comfort_plan()
        routes_page.set_phone(data.PHONE_NUMBER)
        assert routes_page.get_phone()==data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_comfort_plan()
        routes_page.set_phone(data.PHONE_NUMBER)
        routes_page.set_payment(data.CARD_NUMBER, data.CARD_CODE)

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_comfort_plan()
        routes_page.set_phone(data.PHONE_NUMBER)
        routes_page.set_payment(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.set_driver_message(data.MESSAGE_FOR_DRIVER)

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_comfort_plan()
        routes_page.set_phone(data.PHONE_NUMBER)
        routes_page.set_payment(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.set_driver_message(data.MESSAGE_FOR_DRIVER)
        routes_page.set_blanket_sheet()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_comfort_plan()
        routes_page.set_phone(data.PHONE_NUMBER)
        routes_page.set_payment(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.set_driver_message(data.MESSAGE_FOR_DRIVER)
        routes_page.set_blanket_sheet()
        routes_page.set_order_icecreams()

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_comfort_plan()
        routes_page.set_phone(data.PHONE_NUMBER)
        routes_page.set_payment(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.set_driver_message(data.MESSAGE_FOR_DRIVER)
        routes_page.set_blanket_sheet()
        routes_page.set_order_icecreams()
        routes_page.set_order_car()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()