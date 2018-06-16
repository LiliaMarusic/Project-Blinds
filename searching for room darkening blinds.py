from selenium import webdriver
import time
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome("C:\\Users\\Nikolay\\PycharmProjects\\untitled\\driver\\chromedriver.exe")
driver.get("https://www.blinds.com/")
driver.maximize_window()
time.sleep(2)
search = driver.find_element_by_name("q").send_keys("room darkening blinds")
cl = driver.find_element_by_id("gcc-inline-search-submit").click()
lowHigh = driver.find_element_by_link_text("Price Low-High").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 200)")
time.sleep(1)
driver.quit()



