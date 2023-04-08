from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

YEAR = (By.ID ,"years" )

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.ifsc-climbing.org/index.php/world-competition/last-result')

WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.jch-lazyloaded")))
years = Select (WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID , "years"))))

yr = []
for year in years.options:
    yr.append(year.text)
print("Years = ", yr)


#jch-lazyloaded