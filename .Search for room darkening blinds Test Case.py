from selenium import webdriver
import time


driver = webdriver.Chrome("C:\\Users\\Nikolay\\PycharmProjects\\untitled\\driver\\chromedriver.exe")
driver.get("https://www.blinds.com/")
driver.maximize_window()
time.sleep(2)
SearchFld = driver.find_element_by_name("q").send_keys("room darkening blinds")
SearchLoop = driver.find_element_by_xpath("//button[@id='gcc-inline-search-submit']").click()
lowHigh = driver.find_element_by_link_text("Price Low-High").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 200)")
time.sleep(1)
driver.quit()