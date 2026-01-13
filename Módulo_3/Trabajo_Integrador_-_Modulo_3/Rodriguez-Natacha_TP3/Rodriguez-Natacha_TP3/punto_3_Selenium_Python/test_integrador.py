import pytest
import selenium
from selenium.webdriver.common.by import By
from punto_3_Selenium_Python.LoginPage import LoginPage 
from punto_3_Selenium_Python.ProductsPage import ProductsPage
from punto_3_Selenium_Python.CartPage import CartPage
from punto_3_Selenium_Python.CheckoutPage import CheckoutPage

# _____________________________________________________________________
#CASO 1: ORDENAR Y VERIFICAR 

def test_caso_1_ordenar_por_precio(driver_setup):
    driver = driver_setup
    
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    
    # ACCIONES: Login y Ordenamiento
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    products_page.ordenar_por_valor("lohi") # low to high
    
    # VERIFICACIÓN : Obtener lista de precios y compararla
    precios = products_page.obtener_precios()
    
    # La lista obtenida debe ser igual a la lista si la ordenamos 
    assert precios == sorted(precios), "Caso 1 Falló: Los productos no se ordenaron correctamente."

# _______________________________________________________________________
# CASO 2: CHECKOUT CON ERRORES DE VALIDACIÓN
def test_caso_2_checkout_fallido(driver_setup):
    driver = driver_setup
    
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    
    # ACCIONES
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    products_page.agregar_todos_al_carrito()
    products_page.ir_al_carrito()
    cart_page.ir_a_checkout()
    
    # VERIFICACIÓN 1: Solo Nombre _> Espera error de Apellido
    checkout_page.completar_datos(nombre="Juan", apellido="", zip_code="")
    assert checkout_page.obtener_texto_error() == "Error: Last Name is required", "Verificación 1 Falló."

    # VERIFICACIÓN 2: Nombre y Apellido _> Espera error de ZIP
    # El método 'completar_datos' solo envía las keys de las variables pasadas
    checkout_page.completar_datos(nombre="Juan", apellido="Perez", zip_code="")
    assert checkout_page.obtener_texto_error() == "Error: Postal Code is required", "Verificación 2 Falló."


# _______________________________________________________________________
# 3. CASO 3: FLUJO COMPLETO DE COMPRA CON REMOCIÓN Y RE-ADICIÓN
def test_caso_3_flujo_compra_completa(driver_setup):
    driver = driver_setup
    
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    products_page.agregar_todos_al_carrito() 
    products_page.ir_al_carrito()

    # Precondiciones: que el carrito este vacío
    # ACCIÓN Y VERIFICACIÓN 1: Remover y verificar vacío
    cart_page.remover_todos_los_articulos()
    assert cart_page.es_carrito_vacio() is True, "Caso 3 Falló: El carrito no se vació."

    # ACCIONES: Continuar, agregar, checkout
    driver.find_element(By.ID, "continue-shopping").click() 
    products_page.agregar_todos_al_carrito() 
    products_page.ir_al_carrito()
    cart_page.ir_a_checkout()
    
    # COMPLETAR y FINALIZAR
    checkout_page.completar_datos(nombre="Natacha", apellido="Rodriguez", zip_code="5012")
    checkout_page.finalizar_compra()
    
    # VERIFICACIÓN 2: Mensaje final de éxito
    assert checkout_page.obtener_mensaje_final() == "Thank you for your order!", "Caso 3 Falló: El mensaje de éxito no es correcto."