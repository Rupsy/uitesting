from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.888sport.com/tennis/')

players= driver.find_elements(By.XPATH , "//a[@class='event-description event-description--inplay']")

for player in players:
    print(player.text)

