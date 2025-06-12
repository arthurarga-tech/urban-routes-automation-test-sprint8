import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    # ======= Locators =======
    # Campos de endereço
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Seleção de plano
    comfort_plan_card = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    active_plan_card = (By.XPATH, "//div[contains(@class, 'tcard') and contains(@class, 'active')]")
    call_taxi_button = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Chamar um táxi')]")

    # Número de telefone
    phone_number_control = (By.CSS_SELECTOR, '.np-button')
    phone_number_input = (By.ID, 'phone')
    phone_number_code_input = (By.ID, 'code')
    phone_number_next_button = (By.CSS_SELECTOR, 'button.full')
    phone_number_confirm_button = (By.XPATH, "//button[@type='submit' and contains(text(), 'Confirmar')]")
    phone_number = (By.CSS_SELECTOR, '.np-text')

    # Pagamento
    payment_method_select = (By.CSS_SELECTOR, 'div.pp-button.filled')
    add_card_control = (By.XPATH, "//div[@class='pp-title' and text()='Adicionar cartão']")
    card_number_input = (By.ID, 'number')
    card_code_input = (By.XPATH, "//input[@name='code']")
    card_credential_confirm_button = (By.XPATH, "//button[@type='submit' and contains(text(), 'Adicionar')]")
    out_auto_click = (By.XPATH, "//div[@class='section active unusual']")
    close_button_payment_method = (By.CSS_SELECTOR, "div.open.payment-picker button.close-button.section-close")

    # Mensagem para o motorista
    message_for_driver = (By.ID, 'comment')

    # Cobertor e lençol
    option_switches = (By.CSS_SELECTOR, "span.slider.round")
    option_switches_actived = (By.CSS_SELECTOR, "div.switch input.switch-input:checked")

    # Sorvete
    counter_plus_button = (By.CSS_SELECTOR, "div.counter-plus")
    counter_value = (By.CSS_SELECTOR, "div.counter-value")

    # Pedido
    order_car_button = (By.CSS_SELECTOR, "span.smart-button-main")
    pop_up_confirmation = (By.XPATH, "//div[@class='order-header-content']")

    loader = (By.CSS_SELECTOR, '.loader')


    def __init__(self, driver):
        self.driver = driver

    # ======= Métodos utilitários =======
    def wait_for_loader_to_disappear(self):
        """Aguarda o carregador desaparecer (após requisições/ações)"""
        try:
            WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(self.loader))
        except:
            pass

    # ======= Endereço =======
    def set_from(self, from_address):
        """Define o endereço de origem"""
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.from_field))
        field.clear()
        field.send_keys(from_address)

    def get_from(self):
        """Obtém o endereço de origem inserido"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.from_field)
        ).get_property('value')

    def set_to(self, to_address):
        """Define o endereço de destino"""
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.to_field))
        field.clear()
        field.send_keys(to_address)

    def get_to(self):
        """Obtém o endereço de destino inserido"""
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.to_field)
        ).get_property('value')

    def click_call_taxi_button(self):
        """Clica no botão 'Chamar um táxi'"""
        self.wait_for_loader_to_disappear()
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.call_taxi_button))
        self.driver.execute_script("arguments[0].click();", button)

    def set_route(self, from_address, to_address):
        """Preenche origem, destino e clica em 'Chamar um táxi'"""
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_call_taxi_button()

    # ======= Select Confort  =======
    def set_select_comfort_plan(self):
        """Seleciona o plano Comfort se não estiver ativo"""
        comfort_card = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.comfort_plan_card)
        )
        if "active" not in comfort_card.get_attribute("class"):
            comfort_card.click()
            self.wait_for_loader_to_disappear()

    def get_selected_plan_is_comfort(self):
        """Verifica se o plano Comfort está ativo"""
        active_card = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.active_plan_card)
        )
        return "Comfort" in active_card.text

    # ======= Telefone =======
    def set_phone_number(self, number):
        """Insere número de telefone"""
        self.wait_for_loader_to_disappear()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.phone_number_control)
        ).click()
        phone_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.phone_number_input)
        )
        phone_input.clear()
        phone_input.send_keys(number)

    def set_phone_code(self):
        """Preenche o código recebido via SMS"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.phone_number_next_button)
        ).click()
        code = retrieve_phone_code(self.driver)
        code_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.phone_number_code_input)
        )
        code_input.clear()
        code_input.send_keys(code)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.phone_number_confirm_button)
        ).click()

    def set_phone(self, number):
        """Preenche o número e o código de telefone"""
        self.set_phone_number(number)
        self.set_phone_code()

    def get_phone(self):
        """Retorna o número de telefone preenchido"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "phone"))
        )
        return element.get_attribute('value').strip()

    # ======= Pagamento =======
    def set_payment_number(self, card_number):
        """Preenche o número do cartão"""
        self.wait_for_loader_to_disappear()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.payment_method_select)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_card_control)
        ).click()
        number_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.card_number_input)
        )
        number_input.clear()
        number_input.send_keys(card_number)

    def get_card_number(self):
        """Obtém o número do cartão preenchido"""
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.card_number_input)
        ).get_attribute('value')

    def set_payment_code(self, code_number):
        """Preenche o código de segurança do cartão"""
        code_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.card_code_input)
        )
        code_input.clear()
        code_input.send_keys(code_number)

    def get_card_code(self):
        """Obtém o código de segurança do cartão"""
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.card_code_input)
        ).get_attribute('value')

    def set_confirm_credit_card(self):
        """Confirma e fecha o modal de cartão de crédito"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.out_auto_click)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.card_credential_confirm_button)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.close_button_payment_method)
        ).click()

    def set_payment(self, card_number, code_number):
        """Preenche todos os dados de pagamento"""
        self.set_payment_number(card_number)
        self.set_payment_code(code_number)
        self.set_confirm_credit_card()

    # ======= Mensagem para o motorista =======
    def set_driver_message(self, message):
        """Envia uma mensagem ao motorista"""
        self.wait_for_loader_to_disappear()
        field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.message_for_driver)
        )
        field.clear()
        field.send_keys(message)
        assert self.get_driver_message() == message, (
            f"Mensagem esperada '{message}', encontrada '{self.get_driver_message()}'"
        )

    def get_driver_message(self):
        """Retorna a mensagem para o motorista"""
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.message_for_driver)
        ).get_attribute('value')

    # ======= Switch: cobertor e lençol =======
    def set_blanket_sheet(self):
        """Ativa o switch de cobertor e lençol"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.option_switches)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.option_switches_actived)
        )

    def get_blanket_sheet_selected(self):
        """Verifica se o switch está ativado"""
        return self.driver.find_element(*self.option_switches_actived).is_selected()

    # ======= Sorvetes =======
    def set_order_icecreams(self):
        """Adiciona dois sorvetes ao pedido"""
        wait = WebDriverWait(self.driver, 10)
        for _ in range(2):
            wait.until(EC.element_to_be_clickable(self.counter_plus_button)).click()

    def get_icecream_count(self):
        """Retorna a quantidade de sorvetes adicionada"""
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.counter_value)
        ).text

    # ======= Pedido final =======
    def set_order_car(self):
        """Confirma o pedido do carro"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.order_car_button)
        ).click()

    def get_order_confirmation_popup_displayed(self):
        """Verifica se o pop-up de confirmação do pedido está visível"""
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.pop_up_confirmation)
        )
        return element.is_displayed()

