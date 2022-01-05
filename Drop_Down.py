from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")

link = driver.find_element_by_link_text('Dropdown')
link.click()
print(driver.current_url)

select = driver.find_element_by_xpath('/html/body/div[2]/div/div/select')
select.click()

def DropDown_Selected(option):
    Check = option.is_selected()
    if Check == True :
        print(option.text + " is selected")
    else:
        print(option.text + " is not selected")

option1 = driver.find_element_by_xpath('/html/body/div[2]/div/div/select/option[2]')
option1.click()
DropDown_Selected(option1)


option2 = driver.find_element_by_xpath('/html/body/div[2]/div/div/select/option[3]')
option2.click()
DropDown_Selected(option2)

driver.quit()