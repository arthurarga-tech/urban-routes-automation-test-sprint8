import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    # Locators de campos, botões e elementos da interface
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Tarifas
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

    # Pagamentos
    payment_method_select = (By.CSS_SELECTOR, 'div.pp-button.filled')
    add_card_control = (By.XPATH, "//div[@class='pp-title' and text()='Adicionar cartão']")
    card_number_input = (By.ID, 'number')
    card_code_input = (By.XPATH, "//input[@name='code']")
    card_credential_confirm_button = (By.XPATH, "//button[@type='submit' and contains(text(), 'Adicionar')]"'')
    out_auto_click = (By.XPATH, "//div[@class='section active unusual']")
    close_button_payment_method = (By.CSS_SELECTOR, "div.open.payment-picker button.close-button.section-close")

    # Mensagem pro motorista
    message_for_driver = (By.ID, 'comment')

    # Adicionar cobertor e lençóis
    option_switches = (By.CSS_SELECTOR, "span.slider.round")
    option_switches_actived = (By.CSS_SELECTOR, "div.switch input.switch-input:checked")

    # Adicionar 2 sorvetes
    counter_plus_button = (By.CSS_SELECTOR, "div.counter-plus")
    counter_value = (By.CSS_SELECTOR, "div.counter-value")

    # Pedido
    order_car_button = (By.CSS_SELECTOR, "span.smart-button-main")
    loader = (By.CSS_SELECTOR, '.loader')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_loader_to_disappear(self):
        """Espera até o carregador desaparecer"""
        try:
            WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(self.loader))
        except:
            pass

    def set_from(self, from_address):
        """Preenche o campo de origem"""
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.from_field))
        field.clear()
        field.send_keys(from_address)

    def get_from(self):
        """Retorna o valor preenchido no campo de origem"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.from_field)).get_property('value')

    def set_to(self, to_address):
        """Preenche o campo de destino"""
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.to_field))
        field.clear()
        field.send_keys(to_address)

    def get_to(self):
        """Retorna o valor preenchido no campo de destino"""
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.to_field)).get_property('value')

    def click_call_taxi_button(self):
        """Clica no botão para chamar um táxi"""
        self.wait_for_loader_to_disappear()
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.call_taxi_button))
        self.driver.execute_script("arguments[0].click();", button)

    def set_route(self, from_address, to_address):
        """Define a rota com origem e destino"""
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_call_taxi_button()

    def set_select_comfort_plan(self):
        """Seleciona o plano Comfort, se ainda não estiver ativo"""
        comfort_card = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.comfort_plan_card))

        if "active" not in comfort_card.get_attribute("class"):
            comfort_card.click()
            self.wait_for_loader_to_disappear()

    def get_selected_plan_is_comfort(self):
        """Verifica se o plano selecionado é o Comfort"""
        active_card = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.active_plan_card))
        return "Comfort" in active_card.text

    def set_phone_number(self, number):
        """Preenche o número de telefone e o código de verificação"""
        self.wait_for_loader_to_disappear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.phone_number_control)).click()

        phone_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.phone_number_input))
        phone_input.clear()
        phone_input.send_keys(number)

    def get_phone(self):
        """Retorna o número de telefone exibido no input"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "phone")))
        return element.get_attribute('value').strip()

    def set_phone_code(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.phone_number_next_button)).click()
        code = retrieve_phone_code(self.driver)
        code_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.phone_number_code_input))
        code_input.clear()
        code_input.send_keys(code)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.phone_number_confirm_button)).click()

    def set_phone(self, number):
        self.set_phone_number(number)
        self.set_phone_code()

    def set_payment_number(self, card_number):
        self.wait_for_loader_to_disappear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.payment_method_select)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_card_control)).click()

        number_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.card_number_input))
        number_input.clear()
        number_input.send_keys(card_number)

    def get_card_number(self):
        """Retorna o número inserido no campo do cartão"""
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.card_number_input)).get_attribute('value')

    def set_payment_code(self, code_number):
        code_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.card_code_input))
        code_input.clear()
        code_input.send_keys(code_number)

    def get_card_code(self):

        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.card_code_input)).get_attribute('value')

    def set_confirm_credit_card(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.out_auto_click)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.card_credential_confirm_button)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.close_button_payment_method)).click()

    def set_payment(self, card_number, code_number):
        self.set_payment_number(card_number)
        self.set_payment_code(code_number)
        self.set_confirm_credit_card()

    def set_driver_message(self, message):
        """Escreve uma mensagem para o motorista"""
        self.wait_for_loader_to_disappear()
        driver_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.message_for_driver))
        driver_message.clear()
        driver_message.send_keys(message)
        assert self.get_driver_message() == message, f"Mensagem esperada '{message}', encontrada '{self.get_driver_message()}'"

    def get_driver_message(self):
        """Retorna a mensagem inserida para o motorista"""
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.message_for_driver)).get_attribute('value')

    def set_blanket_sheet(self):
        """Ativa o switch de cobertor e lençol."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.option_switches)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.option_switches_actived))

    def get_blanket_sheet_selected(self):
        """Retorna True se o switch de cobertor e lençol estiver ativado."""
        return self.driver.find_element(*self.option_switches_actived).is_selected()

    def set_order_icecreams(self):
        """Adiciona dois sorvetes ao pedido"""
        wait = WebDriverWait(self.driver, 10)
        for _ in range(2):
            wait.until(EC.element_to_be_clickable(self.counter_plus_button)).click()

    def get_icecream_count(self):
        """Retorna a quantidade de sorvetes selecionados"""
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.counter_value)).text

    def set_order_car(self):
        """Finaliza o pedido do carro"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.order_car_button)).click()
