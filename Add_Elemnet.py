from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")

link = driver.find_element_by_link_text('Add/Remove Elements')
link.click()
print(driver.current_url)

AddElement = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
#AddElement = driver.find_elements_by_css_selector('div.example>button')[0]

print(AddElement.text)
if(AddElement.is_displayed):
    print('Element is present')
else:
    print('Element is not present')


AddElement.click()
assert 'Delete' 

#DeleteElement  = driver.find_elements_by_css_selector('div.example>div>button')[0]
DeleteElement = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/button')
print(DeleteElement.text)
DeleteElement.click()


try: 
    DeleteElement = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/button')
    print("Element exist -" + DeleteElement.text)
except NoSuchElementException: print('Element does not exist')

driver.quit()

