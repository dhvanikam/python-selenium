from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")

link = driver.find_element_by_link_text('Dynamic Loading')
link.click()
print(driver.current_url)

#Hidden element
example1 = driver.find_element_by_link_text('Example 1: Element on page that is hidden')
example1.click()

start1 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button')
start1.click()

WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/img')))
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/h4')))

Result1 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/h4')
print('Example 1: Element on page that is hidden')
print(Result1.text)
#Reload
driver.get("http://the-internet.herokuapp.com/")
link = driver.find_element_by_link_text('Dynamic Loading')
link.click()

#Hidden element
example2 = driver.find_element_by_link_text('Example 2: Element rendered after the fact')
example2.click()

start2 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button')
start2.click()

WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/img')))
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/h4')))
#finish > h4
#element = wait.until(element_has_css_class((By.ID, 'finish'), "example"))

Result2 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/h4')
print('Example 2: Element rendered after the fact')
print(Result2.text)
driver.quit()