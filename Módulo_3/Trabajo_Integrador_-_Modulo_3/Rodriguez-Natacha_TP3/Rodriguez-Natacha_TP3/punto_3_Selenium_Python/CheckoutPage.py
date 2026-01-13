from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
class CheckoutPage:

    # Localizadores
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header") # Mensaje final de éxito

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Método para completar los campos y avanzar
    def completar_datos(self, nombre="", apellido="", zip_code=""):
        if nombre:
            self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(nombre)
        if apellido:
            self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(apellido)
        if zip_code:
            self.driver.find_element(*self.POSTAL_CODE_FIELD).send_keys(zip_code)
            
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    # Método para obtener el texto del error
    def obtener_texto_error(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
    
    # Método para finalizar la compra
    def finalizar_compra(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    # Método para verificar el mensaje final
    def obtener_mensaje_final(self):
        return self.driver.find_element(*self.COMPLETE_HEADER).text