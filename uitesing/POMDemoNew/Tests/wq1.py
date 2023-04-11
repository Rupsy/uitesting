import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/maps/@37.0625,-95.677068,3z')
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID , "searchboxinput"))).send_keys("California Burrito " )
##click search button
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID , "searchbox-searchbutton"))).click()
##clicking firrst result
#
time.sleep(20)
data =[]

while True:
    eles = driver.find_elements(By.XPATH  , "//a[@class='hfpxzc']")
    print ("I am here 123" ,  len(eles) )
    try:
        end_element = driver.find_element(By.XPATH , "//span[@class='HlvSq']/div")
        print ("reached the end , no need to scroll ")
        break
    except Exception as e:

        actions = ActionChains(driver)
        for element in eles:
            print ("I am here " , element.get_attribute('href'))
            element.click()
            actions.move_to_element(element).perform()
            time.sleep(2)
