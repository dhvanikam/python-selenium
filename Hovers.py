from selenium import webdriver
import warnings
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
link = driver.find_element_by_link_text('Hovers')
link.click()
print(driver.current_url)

def reload():
    driver.get("http://the-internet.herokuapp.com/")
    driver.maximize_window()
    link = driver.find_element_by_link_text('Hovers')
    link.click()

profilelist = driver.find_elements_by_xpath("//*[@id='content']/div/div[@class='figure']")
print(len(profilelist))
i=1
for profile in profilelist:
    action = ActionChains(driver)
    action.move_to_element(profile)
    time.sleep(3)
    action.perform()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'figcaption')))
    xpathstring = "//*[@id='content']/div/div[{0}]/div/h5".format(str(i))
    username = driver.find_element_by_xpath(xpathstring)
    i += 1
    print(username.text)
    user1 = driver.find_element_by_link_text('View profile')
    # user1.click()
    # reload()
    print(driver.current_url)
driver.quit()
