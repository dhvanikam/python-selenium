from selenium import webdriver
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")

link = driver.find_element_by_link_text('Basic Auth')
link.click()
print(driver.current_url)

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
SuccessMsg = driver.find_element_by_xpath('/html/body/div[2]/div/div/p')
print(SuccessMsg.text)

if (SuccessMsg.text == 'Congratulations! You must have the proper credentials.'):
    print('Test pass')

else:
    print('Test Fail')

driver.quit()