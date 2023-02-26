import time
from gettext import find
from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select



driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://github.com/")
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//a[@href='/login']").click()
driver.find_element(By.ID,"login_field").send_keys('oussadkrimou1@gmail.com')
driver.find_element(By.ID,"password").send_keys('Anella@108')
driver.find_element(By.NAME,"commit").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,'oussad/Localisateus-Web').click()
time.sleep(3)




