from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

def get_exchange_rate():
    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD")
        data = response.json()
        return data["rates"]["CAD"]
    except:
        return None

def get_pricecharting_price(driver, url):
    try:
        driver.get(url)
        time.sleep(1.5)  # Reduced delay
        price_element = driver.find_element(By.ID, "used_price")
        price_text = price_element.find_element(By.CLASS_NAME, "js-price").text.strip()
        usd_price = float(price_text.replace("$", "").replace(",", ""))
        return usd_price
    except:
        return None

# ---------------------------------------------
# List of product URLs
urls = [
    "https://www.pricecharting.com/game/pokemon-journey-together/elite-trainer-box-pokemon-center", #EXAMPLE
    # Add more URLs here
]
# ---------------------------------------------

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

cad_rate = get_exchange_rate()

for url in urls:
    usd = get_pricecharting_price(driver, url)
    if usd and cad_rate:
        cad = round(usd * cad_rate, 2)
        print(cad)
    else:
        print("Error")

driver.quit()
