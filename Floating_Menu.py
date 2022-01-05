from selenium import webdriver
import warnings
from selenium.webdriver.common.keys import Keys
import time

warnings.filterwarnings("ignore", category=DeprecationWarning)

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()

link = driver.find_element_by_link_text('Floating Menu')
link.click()
print(driver.current_url)

def check_menuitems_displyaled():
    menuitems = driver.find_elements_by_xpath('//*[@id="menu"]//a[@href]')
    for item in menuitems:
        link = driver.find_element_by_link_text(item.text)
        if link.is_displayed():
            print(link.text+ ' menuitem is displayed')
        else:
            print(link.text+ ' menuitem is not displayed')

def check_menu_displayed():
    menu = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]')
    if menu.is_displayed():
        print('Menu is displayed')
    else:
        print('Menu not displayed')

Keylist = [Keys.PAGE_DOWN,Keys.DOWN,Keys.PAGE_UP,Keys.UP,Keys.END,Keys.HOME]
for key in Keylist:
    content = driver.find_element_by_tag_name('body')
    print('Pressed' +str(key))
    content.send_keys(key)
    time.sleep(5)
    check_menu_displayed()
    check_menuitems_displyaled()
driver.quit()