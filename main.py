import time

import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        """Configura o WebDriver antes da execução da suíte de testes"""
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        cls.driver = webdriver.Chrome()

        # Verifica se o servidor está acessível
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e em execução.")

    def test_set_route(self):
        """Testa o preenchimento da rota de origem e destino"""
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        """Testa a seleção do plano Comfort"""
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.set_select_comfort_plan()

        assert routes_page.get_selected_plan_is_comfort(), "Erro: o plano Comfort não foi ativado."

    def test_fill_phone_number(self):
        """Testa o preenchimento e confirmação do número de telefone"""
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.set_select_comfort_plan()
        routes_page.set_phone_number(data.PHONE_NUMBER)

        assert routes_page.get_phone() == data.PHONE_NUMBER

        routes_page.set_phone_code()

    def test_fill_card(self):
        """Testa o preenchimento dos dados do cartão de crédito"""
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.set_select_comfort_plan()
        routes_page.set_phone(data.PHONE_NUMBER)

        routes_page.set_payment_number(data.CARD_NUMBER)
        assert routes_page.get_card_number() == data.CARD_NUMBER

        routes_page.set_payment_code(data.CARD_CODE)
        assert routes_page.get_card_code() == data.CARD_CODE

        routes_page.set_confirm_credit_card()

    def test_comment_for_driver(self):
        """Testa o envio de mensagem para o motorista"""
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.set_select_comfort_plan()
        routes_page.set_phone(data.PHONE_NUMBER)
        routes_page.set_payment(data.CARD_NUMBER, data.CARD_CODE)

        routes_page.set_driver_message(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_driver_message() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        """Testa a seleção da opção de cobertor e lençol"""
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.set_select_comfort_plan()
        routes_page.set_phone(data.PHONE_NUMBER)
        routes_page.set_payment(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.set_driver_message(data.MESSAGE_FOR_DRIVER)

        routes_page.set_blanket_sheet()
        assert routes_page.get_blanket_sheet_selected(), "Erro: o switch de cobertor e lençol não está ativado."

    def test_order_2_ice_creams(self):
        """Testa a adição de 2 sorvetes ao pedido"""
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.set_select_comfort_plan()
        routes_page.set_phone(data.PHONE_NUMBER)
        routes_page.set_payment(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.set_driver_message(data.MESSAGE_FOR_DRIVER)
        routes_page.set_blanket_sheet()

        routes_page.set_order_icecreams()
        assert routes_page.get_icecream_count() == "2", f"Esperado '2', mas apareceu '{routes_page.get_icecream_count()}'"

    def test_car_search_model_appears(self):
        """Testa o fluxo completo até o pedido do carro"""
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.set_select_comfort_plan()
        routes_page.set_phone(data.PHONE_NUMBER)
        routes_page.set_payment(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.set_driver_message(data.MESSAGE_FOR_DRIVER)
        routes_page.set_blanket_sheet()
        routes_page.set_order_icecreams()

        routes_page.set_order_car()
        assert routes_page.get_order_confirmation_popup_displayed(), "Erro: Pop-up de confirmação do pedido não foi exibido."
        time.sleep(3)

    @classmethod
    def teardown_class(cls):
        """Finaliza o WebDriver após a execução dos testes"""
        cls.driver.quit()
