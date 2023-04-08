from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.ifsc-climbing.org/index.php/world-competition/last-result')

wait = WebDriverWait(driver, 10)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.jch-lazyloaded")))
years_select = Select(wait.until(EC.visibility_of_element_located((By.ID, "years"))))
wait.until(lambda d: len(years_select.options) > 1)
years_select.select_by_index(1)
league_select = Select(driver.find_element(By.ID, "indexes"))
wait.until(lambda d: len(league_select.options) > 1)
league_select.select_by_index(1)
events_select = Select(driver.find_element(By.ID, "events"))
wait.until(lambda d: len(events_select.options) > 1)
category_select = Select(driver.find_element(By.ID, "categories"))
wait.until(lambda d: len(category_select.options) > 1)
# print(len(events_select.options))

# Extracts the text from the objects and adds to list
years      = [x.text for x in years_select.options]
leagues    = [x.text for x in league_select.options[1:]]
events     = [x.text for x in events_select.options[1:]]
categories = [x.text for x in category_select.options[1:]]

print(years)
print(leagues)
print(events)
print(categories)

driver.quit()
