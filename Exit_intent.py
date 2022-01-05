from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import MoveTargetOutOfBoundsException
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
link = driver.find_element_by_link_text('Exit Intent')
link.click()
print(driver.current_url)
position = driver.get_window_position()
print(position)

# def mouse_out_viewport():
#     element = driver.find_element_by_xpath('/html/body/div[2]/a/img')
#     try:
#         action = ActionChains(driver)
#         action.move_to_element(element)
#         #action.move_by_offset(-1, -1)
#         time.sleep(30)
#         action.release()
#         action.perform()
#     except MoveTargetOutOfBoundsException as Exception:
#         print('target out of bound***')

def Check_Modal_window_open():
    if EC.new_window_is_opened:
        return True
    else :
        return False

def Close_modal_wondow():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[3]/p')))
    close_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[3]/p')
    close_button.click()



try:
    element = driver.find_element_by_xpath('/html/body/div[2]/a/img')
    print(element.location)
    action = ActionChains(driver)
    action.move_to_element(element)
    action.move_by_offset(2092, -1)
    time.sleep(20)
    action.perform()

    Check = Check_Modal_window_open()
    if Check == True:
        print('New window is opened')
        Close_modal_wondow()
    else:
        print('New window is not opened')
except MoveTargetOutOfBoundsException as Exception:
    Check = Check_Modal_window_open()
    if Check == True:
        print('New window is opened')
        Close_modal_wondow()
    else:
        print('New window is not opened')
  
driver.quit()
