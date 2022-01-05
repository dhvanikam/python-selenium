from selenium import webdriver
import warnings
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import StaleElementReferenceException

warnings.filterwarnings("ignore", category=DeprecationWarning)

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
link = driver.find_element_by_link_text('Frames')
link.click()
print(driver.current_url)

Nested_frames = driver.find_element_by_link_text('Nested Frames')
Nested_frames.click()
framelist = driver.find_elements_by_xpath('/html/frameset/frame')
print(len(framelist))

frameno = 0
for frame in framelist:
    driver.switch_to.default_content()
    print('Frame name:' + frame.get_attribute('name'))
    driver.switch_to.frame(frame.get_attribute('name'))
    nestedframelist = driver.find_elements_by_tag_name('frame')
    print('Total nested frames are :' + str(len(nestedframelist)))
    if len(nestedframelist) == 0:
        print(driver.find_element_by_xpath("/html/body").text)
    else:
        for nframe in nestedframelist:
            driver.switch_to.default_content()
            driver.switch_to.frame(frame.get_attribute('name'))
            print('Nested Frame name:' + nframe.get_attribute('name'))
            driver.switch_to.frame(nframe.get_attribute('name'))
            print(driver.find_element_by_xpath("/html/body").text)
     
    # nestedframes= driver.find_element_by_name(frame.get_attribute('name'))

    # try:
    #     print(driver.find_element_by_name(frame.get_attribute('name')).text)
    #     print(driver.find_element_by_xpath("/html/body").text)      
    # except StaleElementReferenceException as exception:
# driver.switch_to.frame("frame-bottom")
# print(driver.find_element_by_xpath("/html/body").text)
# driver.switch_to.default_content()
# driver.switch_to.frame("frame-top")
# driver.switch_to.frame("frame-left")
# print(driver.find_element_by_xpath("/html/body").text)

# driver.switch_to.default_content()
# driver.switch_to.frame("frame-top")
# driver.switch_to.frame("frame-middle")
# print(driver.find_element_by_xpath("/html/body").text)

# driver.switch_to.default_content()
# driver.switch_to.frame("frame-top")
# driver.switch_to.frame("frame-right")
# print(driver.find_element_by_xpath("/html/body").text)
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
link = driver.find_element_by_link_text('Frames')
link.click()
iframe = driver.find_element_by_link_text('iFrame')
iframe.click()
print(driver.current_url)
driver.switch_to.frame('mce_0_ifr')
time.sleep(2)
print(driver.find_element_by_xpath("/html/body/p").text)
driver.quit()