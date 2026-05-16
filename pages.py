from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

import helpers


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxy_button = (By.CSS_SELECTOR, 'button.button.round')
    comfort_button = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    comfort_selected = (By.XPATH, "//div[contains(@class, 'tcard') and text() = 'Comfort']/..")
    credit_card = (By.XPATH, "//div[@class='pp-value-text' and text() = 'Tarjeta']")
    select_pay_method = (By.XPATH, "//div[@class='pp-text' and text() = 'Método de pago']")
    select_credit_card_button = (By.XPATH, "//div[@class='pp-title' and text() = 'Agregar tarjeta']")
    select_add_credit_card_button = (By.XPATH, "//div[@class='button full disabled' and text() = 'Agregar']")
    imagen_tarjeta = (By.XPATH, "//div[@class='plc']")
    select_add_credit_card_button_blue = (By.XPATH, "//button[@class='button full' and text() = 'Agregar']")
    click_close_button = (By.XPATH, "(//button[@class='close-button section-close'])[3]")

    phone_button = (By.XPATH, "//div[contains(text(),'Número de teléfono')]/ancestor::div[contains(@class,'np-button')]")
    phone_field = (By.ID, "phone")
    phone_code_field = (By.ID, 'code')
    phone_number_confirmation = (By.CLASS_NAME, 'np-text')
    card_number_field = (By.ID, 'number')
    card_cvv_field = (By.XPATH, "//input[@id='code']")
    card_link_button = (By.XPATH, "//button[contains(@class,'link')]")

    message_field = (By.ID, 'comment')
    blanket_checkbox = (By.XPATH, "((//input[@class='switch-input'])[1])/parent::*")
    tissues_checkbox = (By.XPATH, "((//input[@class='switch-input'])[2])/parent::*")
    verify_blanket_checkbox = (By.XPATH, "(//input[@class='switch-input'])[1]")
    verify_tissues_checkbox = (By.XPATH, "(//input[@class='switch-input'])[2]")
    icecream_counter = (By.XPATH, "(//div[@class='counter-value'])[1]")
    add_icecream = (By.XPATH, "(//div[@class='counter-plus'])[1]")

    order_taxi_button = (By.XPATH, "//button[@class='smart-button']")
    search_modal = (By.XPATH, "//div[contains(@class,'order-header-title')]")
    driver_info = (By.XPATH, "(//div[contains(@class,'order-btn-group')]/div)[2]")
    order_time = (By.XPATH, "//div[contains(@class,'order-header-time')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # 🔥 FIX CRÍTICO
    def _safe_type(self, locator, text):
        field = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", field)
        self.driver.execute_script("arguments[0].focus();", field)
        field.clear()
        field.send_keys(text)

    def set_from(self, from_address):
        self._safe_type(self.from_field, from_address)

    def set_to(self, to_address):
        self._safe_type(self.to_field, to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def is_enable_request_taxi_button(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.request_taxy_button)
        ).is_enabled()

    def click_request_taxy(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.request_taxy_button))
        self.driver.find_element(*self.request_taxy_button).click()

    def select_comfort(self):
        comfort = self.wait.until(
            EC.presence_of_element_located(self.comfort_button)
        )
        self.driver.execute_script("arguments[0].click();", comfort)

    def get_comform_selected_class(self):
        return self.wait.until(
            EC.presence_of_element_located(self.comfort_selected)
        ).get_attribute("class")

    def open_phone_form(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.phone_button))
        self.driver.find_element(*self.phone_button).click()

    def set_phone(self, phone):
        self.open_phone_form()

        phone_input = self.wait.until(
            EC.visibility_of_element_located(self.phone_field)
        )
        phone_input.send_keys(phone)
        phone_input.send_keys(Keys.ENTER)
        sms_code = helpers.retrieve_phone_code(self.driver)
        code_input = self.wait.until(
            EC.presence_of_element_located(self.phone_code_field)
        )
        code_input.send_keys(sms_code)
        code_input.send_keys(Keys.ENTER)

    def get_phone_number(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.phone_number_confirmation))
        return self.driver.find_element(*self.phone_number_confirmation).text

    def add_credit_card(self, number, cvv):
        self.driver.find_element(*self.select_pay_method).click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.select_credit_card_button))
        self.driver.find_element(*self.select_credit_card_button).click()

        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.card_number_field))
        self.driver.find_element(*self.card_number_field).send_keys(number+Keys.TAB+cvv)
        self.driver.implicitly_wait(2)
        self.driver.find_element(*self.imagen_tarjeta).click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(*self.select_add_credit_card_button_blue).click()
        self.driver.find_element(*self.click_close_button).click()

    def set_message(self, message):
        msg_input = self.wait.until(
            EC.presence_of_element_located(self.message_field)
        )
        msg_input.send_keys(message)

    def get_comment(self):
        return self.driver.find_element(*self.message_field).get_property('value')

    def request_blanket_and_tissues(self):
        elemento = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.blanket_checkbox))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elemento)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.blanket_checkbox)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.tissues_checkbox)).click()

    def get_blanket(self):
        buttons = self.driver.find_element(*self.verify_blanket_checkbox)
        return buttons.get_property('checked')

    def get_tissues(self):
        buttons = self.driver.find_element(*self.verify_tissues_checkbox)
        return buttons.get_property('checked')

    def add_icecreams(self, count=2):
        plus_btn = self.wait.until(
            EC.element_to_be_clickable(self.add_icecream)
        )
        for _ in range(count):
            plus_btn.click()

    def get_icecreams(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.icecream_counter))
        return self.driver.find_element(*self.icecream_counter).text

    def order_taxi(self):
        self.wait.until(
            EC.element_to_be_clickable(self.order_taxi_button)
        ).click()

    def wait_for_search_modal(self):
        self.wait.until(
            EC.visibility_of_element_located(self.search_modal)
        )

    def return_search_modal(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.search_modal))
        return self.driver.find_element(*self.search_modal).text

    def time_info(self):
        WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located(self.order_time))
        self.driver.find_element(*self.order_time)

    def wait_for_driver_info(self):
        self.wait.until(
            EC.visibility_of_element_located(self.driver_info)
        )

    def return_driver_info(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.driver_info))
        return self.driver.find_element(*self.driver_info).text

    def get_card(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.credit_card))
        return self.driver.find_element(*self.credit_card).text
