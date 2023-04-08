import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('excludeSwitches', ['enable-automation'])

options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options, executable_path='Users/home/Downloads/chromeDriver110')

driver.implicitly_wait(10)
DejeroControlVideo1 = "https://control.dejero.com/return_video/9I_HsFn7NYHiKvtJbHa3WQ"
driver.get(DejeroControlVideo1)
PreviewSwitch = driver.find_element(By.XPATH, "//span[text()='ON']")
PreviewSwitch.click()
print("preview")
FullscreenButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//i[contains(@ng-hide,'isFullscreen || isFullWindow')])[1]")))
FullscreenButton.click()
print("full screen")