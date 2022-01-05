from selenium import webdriver
import warnings
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

warnings.filterwarnings("ignore", category=DeprecationWarning)

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()

link = driver.find_element_by_link_text('Form Authentication')
link.click()
print(driver.current_url)

usernamelist = ['tomsmith', 'abc']
passwordlist = ['SuperSecretPassword!','abc']

for user in usernamelist:
    for pswd in passwordlist:
        username = driver.find_element_by_id('username')
        username.send_keys(user)
        password = driver.find_element_by_id('password')
        password.send_keys(pswd)
        time.sleep(5)
        login = driver.find_element_by_xpath('//*[@class="radius"]') 
        login.click()
        try:
            logout = driver.find_element_by_xpath('//*[@class="button secondary radius"]')
            if logout.is_displayed:
                print('success username:' + str(user) + ' password:'+ str(pswd))
                logout.click()
                print('you are logged out')         
        except NoSuchElementException as exception:
            if user == 'tomsmith' and pswd !='SuperSecretPassword!':
                print('wrong password : username:' + str(user) + ' password:'+ str(pswd))
                # Errormsg = driver.find_element_by_xpath('/html/body/div[1]/div/div/text()')
                # print(Errormsg.text)
            else:
                print('wrong username:' + str(user) + ' password:'+ str(pswd))
                #  Errormsg = driver.find_element_by_xpath('/html/body/div[1]/div/div/text()')
                #  print(Errormsg.text)

driver.quit()