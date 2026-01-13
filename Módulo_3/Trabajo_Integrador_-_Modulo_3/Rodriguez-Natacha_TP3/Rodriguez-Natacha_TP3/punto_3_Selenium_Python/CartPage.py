from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPage:

    # Localizadores
    ITEM_CONTAINERS = (By.CLASS_NAME, "cart_item") 
    # Selector del botón "Remove" genérico
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']") 
    CHECKOUT_BUTTON = (By.ID, "checkout")
    ITEM_CONTAINERS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Método para remover todos los artículos (Requisito Caso 3)
    def remover_todos_los_articulos(self):
        while True:
            try:
                remove_btn = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(self.REMOVE_BUTTON)
                )
                
                remove_btn.click()
                WebDriverWait(self.driver, 5).until(
                    EC.staleness_of(remove_btn)
                )

            except TimeoutException:
                # Si no hay más botones para remover, salimos del ciclo
                break
            except Exception as e:
                # Manejamos otras excepciones (como StaleElementReferenceException) y salimos
                if "no such element" in str(e).lower() or "stale element" in str(e).lower():
                    break
                else:
                    # Si es otro error, lo mostramos
                    print(f"Error inesperado al remover: {e}")
                    break
        
    # Método de verificación de lógica de carrito vacío (Requisito Caso 3)
    def es_carrito_vacio(self) -> bool:
        # find_elements() devuelve una lista vacía si no encuentra elementos
        items = self.driver.find_elements(*self.ITEM_CONTAINERS) 
        return len(items) == 0 # Retorna True si la longitud es 0
            
    def ir_a_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()