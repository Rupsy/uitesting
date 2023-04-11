import time
from concurrent.futures import thread

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/maps/@37.0625,-95.677068,3z')
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID , "searchboxinput"))).send_keys("Bata")
##click search button
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID , "searchbox-searchbutton"))).click()
##clicking firrst result
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH , "//a[@class='hfpxzc']"))).click()

def scrape_result():
    i = 0

    while True:
        # scroll the page until it ends
        last_height = driver.execute_script("return document.documentElement.scrollHeight") +i
        print("last_height >>>>> " , last_height)
        # Scroll to the bottom of page
        driver.execute_script("window.scrollTo(0, arguments[0]);", last_height  )
        # Wait for new videos to show up
        time.sleep(1)
        # Calculate new document height and compare it with last height
        new_height = driver.execute_script("return document.documentElement.scrollHeight") + i
        print("new_height >>>>> " , new_height)
        i = i + 500
        last_height = new_height
        if i == 1000:
            break

    time.sleep(2)
    results = driver.find_elements(By.XPATH, "//div[@class='Nv2PK tH5CWc THOPZb ']")
    print(f"total videos: {len(results)}")
    links = []
    for res in results:
        print("links >>>>> " , res.text)
        ##link = res.find_elements(By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'a').get_attribute('href')
        link = res.find_element(By.TAG_NAME, 'a').get_attribute('href')
        links.append(link)
    return links

scrape_result()