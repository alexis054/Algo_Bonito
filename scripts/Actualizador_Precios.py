from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")  # Ruta a chromedriver

# Configurar navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Opcional: sin ventana
driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)

# URL del producto (reemplazar con la real)
url = "https://www.nuevasluces.com.ar/insumos-para-velas/cera/cera-de-soja-astra-bpf"
driver.get(url)

try:
    # Esperar a que se pueda hacer clic en la opción de 20kg
    btn_20kg = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "20kg")]'))
    )
    btn_20kg.click()

    # Esperar a que aparezca el precio actualizado
    precio_elemento = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-vip__price-value"))
    )

    print("Precio para 20kg:", precio_elemento.text)

finally:
    driver.quit()
