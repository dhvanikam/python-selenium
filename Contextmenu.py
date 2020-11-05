from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")

link = driver.find_element_by_link_text('Context Menu')
link.click()
print(driver.current_url)

Context_menu =  driver.find_element_by_id('hot-spot')
action = ActionChains(driver)
action.context_click(Context_menu).perform()

alert = driver.switch_to.alert
print('Press OK')
alert.accept()

driver.close()