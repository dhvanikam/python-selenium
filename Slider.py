from selenium import webdriver
import warnings
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
link = driver.find_element_by_link_text('Horizontal Slider')
link.click()
print(driver.current_url)

def Move_with_right_key():
    slider = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/input')
    x = slider.location
    print(x)
    action = ActionChains(driver)
    action.move_to_element_with_offset(slider, 635, 163)
    action.click()
    action.perform()
    time.sleep(2)
    slider_span = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/span')
    span = float(slider_span.text)
    while span != 5:
        print('Pressed Arrow Right\n')
        slider.send_keys(Keys.ARROW_RIGHT)
        span +=0.5
        print('slider span is : ' + slider_span.text)

def Move_with_left_key():
    slider = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/input')
    x = slider.location
    print(x)
    action = ActionChains(driver)
    action.move_to_element_with_offset(slider, 635, 163)
    action.click()
    action.perform()
    time.sleep(2)
    slider_span = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/span')
    span = float(slider_span.text)
    while span != 0:
        print('Pressed Arrow left\n')
        slider.send_keys(Keys.ARROW_LEFT)
        span -=0.5
        print('slider span is : ' + slider_span.text)

def Click_drag_slider():
    slider = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/input')
    x = slider.location
    print(x)
    action = ActionChains(driver)
    action.move_to_element_with_offset(slider, 635, 163)
    action.click()
    action.perform()
    time.sleep(2)
    slider_span = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/span')
    span = float(slider_span.text)
    i = -40
    while span <= 5:
        print('drag and drop slider')
        action.drag_and_drop_by_offset(slider, i, 0)
        action.perform()
        i += 10
        span +=0.5
        print('slider span is : ' + slider_span.text + '\n')
  
#Set the focus on the slider (by clicking on it) and use the arrow keys to move it right and left.

###ARROW RIGHT KEY
Move_with_right_key()

###ARROW LEFT KEY
Move_with_left_key()

# # click and drag the slider with your mouse
Click_drag_slider()

driver.quit()