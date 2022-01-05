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

link = driver.find_element_by_link_text('Dynamic Controls')
link.click()
print(driver.current_url)

def Checkbox_present(Checkbox):
    try:
        Check = Checkbox.is_displayed()
        if Check == True :
            print('Checkbox exist')
        else:
            print('Checkbox does not exist')
    except StaleElementReferenceException as Exception:
        print('Checkbox does not exist')

def Checkbox_Resultmsg():
    wait = WebDriverWait(driver, 10)
    element2 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/p')))
    Msg = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[1]/p')
    print(Msg.text)

def Textbox_enabled(Textbox):
    try:
        Check = Textbox.is_enabled()
        if Check == True :
            print('Textbox is enabled')
        else:
            print('Textbox is disabled')
    except StaleElementReferenceException as Exception:
        print('Textbox disabled')

def Textbox_Resultmsg():
    wait = WebDriverWait(driver, 10)
    element2 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/p')))
    Msg = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[2]/p')
    print(Msg.text)

# Checkbox
Checkbox = driver.find_element_by_id('checkbox')
print("checking checkbox exist")
Checkbox_present(Checkbox)

#Remove checkbox
print("\nPressed Remove button")
RemoveButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[1]/button')
RemoveButton.click()
Checkbox_Resultmsg()
Checkbox_present(Checkbox)

#Add checkbox
print("\nPressed ADD button")
AddButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[1]/button')
AddButton.click()
Checkbox_Resultmsg()
Checkbox = driver.find_element_by_id('checkbox')
Checkbox_present(Checkbox)

# Textbox
Textbox = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[2]/input')
print("checking textbox enabled")
Textbox_enabled(Textbox)

#Enable textbox
print("\nPressed Enable button")
EnableButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[2]/button')
EnableButton.click()
Textbox_Resultmsg()
Textbox_enabled(Textbox)

#Disable textbox
print("\nPressed disabled button")
DisableButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[2]/button')
DisableButton.click()
Textbox = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[2]/input')

Textbox_Resultmsg()
Textbox_enabled(Textbox)

driver.quit()