import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # Importar para configurar Chrome

# 1. Cambiar el scope a "function" para aislar cada test (CRÍTICO)
@pytest.fixture(scope="function")
def driver_setup():
    """
    Inicializa el driver de Chrome en modo Incógnito para evitar modales
    de guardado de contraseña y abre una sesión limpia por cada test.
    """
    # 2. Configurar Options
    opts = Options()
    
    # Modo incógnito por el modal de contraseña que frena los tests
    opts.add_argument("--incognito") 
    
    # Opciones para deshabilitar gestores de contraseña (como respaldo, aunque Incógnito ayuda mucho)
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    
    # 3. Setup: Inicializa el driver con las opciones
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts) # Pasar 'options=opts'
    
    # Espera implícita
    driver.implicitly_wait(5) 
    
    # 4. Yield: Cede el driver al test
    yield driver
    
    # 5. Teardown: Cierra el driver después de CADA test
    driver.quit()