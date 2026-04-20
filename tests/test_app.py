from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def test_add_employee():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get("http://3.110.163.78:5000")

    name_box = driver.find_element(By.ID, "name")
    name_box.send_keys("Sai Kumar")

    driver.find_element(By.ID, "addBtn").click()

    time.sleep(2)

    body = driver.page_source

    assert "Sai Kumar" in body

    driver.quit()
