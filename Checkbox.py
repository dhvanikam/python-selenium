from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")

link = driver.find_element_by_link_text('Checkboxes')
link.click()
print(driver.current_url)

def Checkbox_checked(Checkbox, name):
    Check = Checkbox.is_selected()
    # Check_text = 'Checkbox ' + str(num)
    print(Check)
    if Check == True :
        print(name + " is checked")
    else:
        print(name + " is unchecked")

# Checkbox 1
Checkbox1 = driver.find_element_by_xpath('/html/body/div[2]/div/div/form/input[1]')
text1 = driver.find_element_by_xpath("//*[@id='checkboxes']").text.split('\n')
Checkbox_checked(Checkbox1, text1[0])
Checkbox1.click()
Checkbox_checked(Checkbox1, text1[0])

#Checkbox 2
Checkbox2 = driver.find_element_by_xpath('/html/body/div[2]/div/div/form/input[2]')
Checkbox_checked(Checkbox2, text1[1])
Checkbox2.click()
Checkbox_checked(Checkbox2, text1[1])

