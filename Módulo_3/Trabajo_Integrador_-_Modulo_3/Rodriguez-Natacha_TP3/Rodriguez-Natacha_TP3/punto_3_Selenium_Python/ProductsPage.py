# ProductsPage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select 

class ProductsPage:
    
    # Localizadores
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    PRICE_ELEMENTS = (By.CLASS_NAME, "inventory_item_price")
    
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[text()='Add to cart']")
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, "a.shopping_cart_link") 
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Método para ordenar (Requisito Caso 1)
    def ordenar_por_valor(self, valor_orden="lohi"): # lohi = low to high
        select_element = Select(self.driver.find_element(*self.SORT_SELECT))
        select_element.select_by_value(valor_orden)
        
    # Método para obtener los precios y verificar el orden (Requisito Caso 1)
    def obtener_precios(self) -> list[float]:
        price_elements = self.driver.find_elements(*self.PRICE_ELEMENTS)
        precios = []
        for element in price_elements:
            # Limpiar el texto '$29.99' a float 29.99 
            precio_texto = element.text.replace('$', '')
            precios.append(float(precio_texto))
        return precios
        
    # Método para agregar todos los elementos (Requisito Caso 2)
    def agregar_todos_al_carrito(self):
        botones = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        # Iterar sobre la lista y hacer click en cada uno (Clase 4: Ciclo for)
        for boton in botones:
            boton.click()
            
    # Método para ir al carrito (Requisito Caso 2 y 3)
    def ir_al_carrito(self):
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()