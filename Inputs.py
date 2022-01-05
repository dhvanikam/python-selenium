from selenium import webdriver
import warnings
from selenium.webdriver.common.keys import Keys
import time

warnings.filterwarnings("ignore", category=DeprecationWarning)

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
link = driver.find_element_by_link_text('Inputs')
link.click()
print(driver.current_url)
input = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/input')
input.send_keys(Keys.NUMPAD1)
time.sleep(2)
input.send_keys(Keys.ARROW_UP)
time.sleep(2)
input.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
print(input.text)
driver.quit()