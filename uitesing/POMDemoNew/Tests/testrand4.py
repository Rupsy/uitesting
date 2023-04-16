import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/maps/@37.0625,-95.677068,3z')
time.sleep(20)
sign_ele = driver.find_element(By.ID , "gb_70")
sign_ele.click()

time.sleep(5)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH , "//input[@id='identifierId']"))).send_keys("sam15042023@gmail.com")
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH , "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']"))).click()


WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH , "//input[@name='Passwd']"))).send_keys("$$$$$$$")
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH , "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']"))).click()


WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID , "searchboxinput"))).send_keys("HANWANT MAHAL, JODHPUR  " )


##click search button
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID , "searchbox-searchbutton"))).click()
##clicking firrst result

while True:
    eles = driver.find_elements(By.XPATH  , "//div[@class='lMbq3e']")
    try:
        actions = ActionChains(driver)

        write_review_element = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH , "//span[contains(text(),'Write a review')]")))
        actions.move_to_element(write_review_element).perform()
        write_review_element.click()
        time.sleep(5)
        break

    except Exception as e:
        print("Excdeption " , e)


multi_window = driver.current_window_handle
print("Number of window open: ", multi_window)
driver.switch_to.window(multi_window)


WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME , "goog-reviews-write-widget")))
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH , "//span[contains(text(),'Posting publicly')]"))).click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH , "//div[@class='s2xyy'][@aria-label='Four stars']"))).click()
time.sleep(5)

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR , "#c1"))).send_keys("Loved the place.Its awesome !!")
time.sleep(5)

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH , "//button[@jsname='IJM3w']"))).click()
print ("comment added")