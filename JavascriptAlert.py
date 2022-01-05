from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")

link = driver.find_element_by_link_text('JavaScript Alerts')
link.click()
print(driver.current_url)

#JS ALert Press OK
print('JS Alert Test')
JSalert = driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[1]/button')
JSalert.click()
alert = driver.switch_to.alert
print('Press OK')
alert.accept()
SuccessMsg = driver.find_element_by_xpath('/html/body/div[2]/div/div/p[2]')
print(SuccessMsg.text)

if (SuccessMsg.text == 'You successfuly clicked an alert'):
    print('JS Alert Test pass\n')

else:
    print('JS Alert Test fail')

#JS Confirm Alert Press OK
print('JS Confirm Test Press OK')
JSConfirm = driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[2]/button')
JSConfirm.click()
alert = driver.switch_to.alert
print('Press OK')
alert.accept()

SuccessMsg = driver.find_element_by_xpath('/html/body/div[2]/div/div/p[2]')
print(SuccessMsg.text)

if (SuccessMsg.text == 'You clicked: Ok'):
    print('JS Confirm press OK Test pass\n')

else:
    print('JS Confirm press OK Test fail')

#JS Confirm Alert Press Cancel
print('JS Confirm Test Press Cancel')
JSConfirm = driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[2]/button')
JSConfirm.click()
alert = driver.switch_to.alert
print('Press cancel')
alert.dismiss()

SuccessMsg = driver.find_element_by_xpath('/html/body/div[2]/div/div/p[2]')
print(SuccessMsg.text)

if (SuccessMsg.text == 'You clicked: Cancel'):
    print('JS Confirm press Cancel Test pass\n')

else:
    print('JS Confirm press Cancel Test Fail')

#JS Prompt OK
print('JS Prompt Test Press OK')
JSPrompt = driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[3]/button')
JSPrompt.click()
alert = driver.switch_to.alert
print('Enter admin')
alert.send_keys('admin')
print('Press OK')
alert.accept()

SuccessMsg = driver.find_element_by_xpath('/html/body/div[2]/div/div/p[2]')
print(SuccessMsg.text)
if (SuccessMsg.text == 'You entered: admin'):
    print('JS Prompt press OK Test pass\n')
else:
    print('JS Prompt press OK Test Fail')

#JS Prompt Cancel
print('JS Prompt Test Press Cancel')
JSPrompt = driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[3]/button')
JSPrompt.click()
alert = driver.switch_to.alert
print('Enter admin')
alert.send_keys('admin')
print('Press Cancel')
alert.dismiss()

SuccessMsg = driver.find_element_by_xpath('/html/body/div[2]/div/div/p[2]')
print(SuccessMsg.text)
if (SuccessMsg.text == 'You entered: null'):
    print('JS prompt Press Cancel Test pass\n')
else:
    print('JS prompt Press Cancel Test Fail')

driver.quit()