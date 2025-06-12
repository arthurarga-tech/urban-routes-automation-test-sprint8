import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

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

    payment_method_select = (By.CSS_SELECTOR, 'div.pp-button.filled')
    add_card_control = (By.XPATH, "//div[@class='pp-title' and text()='Adicionar cartão']")
    card_number_input = (By.ID, 'number')
    card_code_input = (By.XPATH, "//input[@name='code']")
    out_auto_click = (By.XPATH, "//div[@class='section active unusual']")
    close_button_payment_method = (By.CSS_SELECTOR, "div.open.payment-picker button.close-button.section-close")

    message_for_driver = (By.ID, 'comment')

    option_switches = (By.CSS_SELECTOR, "span.slider.round")
    option_switches_actived = (By.CSS_SELECTOR, "div.switch input.switch-input:checked")

    counter_plus_button = (By.CSS_SELECTOR, "div.counter-plus")
    counter_value = (By.CSS_SELECTOR, "div.counter-value")

    # Pedido
    order_car_button = (By.CSS_SELECTOR, "span.smart-button-main")
    loader = (By.CSS_SELECTOR, '.loader')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_loader_to_disappear(self):
        try:
            WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(self.loader))
        except:
            pass

    def set_from(self, from_address):
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.from_field))
        field.clear()
        field.send_keys(from_address)

    def get_from(self):

    def set_to(self, to_address):
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.to_field))
        field.clear()
        field.send_keys(to_address)

    def get_to(self):

    def click_call_taxi_button(self):
        self.wait_for_loader_to_disappear()
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.call_taxi_button))
        self.driver.execute_script("arguments[0].click();", button)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_call_taxi_button()

    def set_select_comfort_plan(self):
        if "active" not in comfort_card.get_attribute("class"):
            comfort_card.click()
            self.wait_for_loader_to_disappear()

    def get_selected_plan_is_comfort(self):
        return "Comfort" in active_card.text

    def set_phone_number(self, number):
        self.wait_for_loader_to_disappear()
        phone_input.clear()
        phone_input.send_keys(number)

    def set_phone_code(self):
        code = retrieve_phone_code(self.driver)
        code_input.clear()
        code_input.send_keys(code)

    def set_phone(self, number):
        self.set_phone_number(number)
        self.set_phone_code()

    def set_payment_number(self, card_number):
        self.wait_for_loader_to_disappear()
        number_input.clear()
        number_input.send_keys(card_number)

    def get_card_number(self):

    def set_payment_code(self, code_number):
        code_input.clear()
        code_input.send_keys(code_number)

    def get_card_code(self):

    def set_confirm_credit_card(self):

    def set_payment(self, card_number, code_number):
        self.set_payment_number(card_number)
        self.set_payment_code(code_number)
        self.set_confirm_credit_card()

    def set_driver_message(self, message):
        self.wait_for_loader_to_disappear()

    def get_driver_message(self):

    def set_blanket_sheet(self):

    def get_blanket_sheet_selected(self):
        return self.driver.find_element(*self.option_switches_actived).is_selected()

    def set_order_icecreams(self):
        """Adiciona dois sorvetes ao pedido"""
        wait = WebDriverWait(self.driver, 10)
        for _ in range(2):
            wait.until(EC.element_to_be_clickable(self.counter_plus_button)).click()

    def get_icecream_count(self):

    def set_order_car(self):
