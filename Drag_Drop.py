from selenium import webdriver
import warnings
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.alert import Alert

warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome()


driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/drag_and_drop")
Source = driver.find_element_by_css_selector('#column-a')
Target = driver.find_element_by_css_selector('#column-b')
x = Source.location
y = Target.location
print(x)
print(y)
# y = BoxB.location 
action1 = ActionChains(driver)
# action1.move_to_element(Source).click_and_hold().move_to_element(Target).release().perform()
action1.move_to_element_with_offset(Source, 850, 89)
# action1.move_to_element(Source)
# action1.move_to_element(Source)
# time.sleep(2)
# action1.click_and_hold(Source)
# time.sleep(2)
# action1.move_to_element_with_offset(Target, 330, 89)
# time.sleep(2)
# action1.release()
# action1.perform()
# action1.drag_and_drop(Source, Target).perform()
# action1.move_to_element_with_offset(Source, Source.location.get('x'), Source.location.get('y'))
# action1.move_to_element_with_offset(Source, 640, 80)
# action1.drag_and_drop(Source, Target).perform()
# time.sleep(3)
action1.move_to_element(Target)
action1.drag_and_drop_by_offset(Source, 250, 0)
action1.perform()
time.sleep(5)

Header = driver.find_element_by_xpath('//*[@id="column-b"]/header')
print(Header.text)
print(Target.text)
driver.quit()
