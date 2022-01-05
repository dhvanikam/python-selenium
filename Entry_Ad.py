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

link = driver.find_element_by_link_text('Entry Ad')
link.click()
print(driver.current_url)


def Check_Modal_window_open():
    if EC.new_window_is_opened:
        return True
    else :
        return False

def Close_modal_wondow():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[3]/p')))
    close_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[3]/p')
    close_button.click()

Check = Check_Modal_window_open()
if Check == True:
    print('New window is opened')
    Close_modal_wondow()
else:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/p[3]/a')))
    Click_here = driver.find_element_by_id('restart-ad')
    Click_here.click()
    new_window = driver.find_element_by_class_name('modal')
    print('New window is opened')
    Close_modal_wondow()
driver.quit()
