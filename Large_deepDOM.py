from selenium import webdriver
import warnings
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import StaleElementReferenceException
import re


warnings.filterwarnings("ignore", category=DeprecationWarning)

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
link = driver.find_element_by_link_text('Large & Deep DOM')
link.click()
print(driver.current_url)

siblinglist = driver.find_elements_by_xpath("//*[@class='parent large-12 large-centered columns']//div[starts-with(@class,'parent')]")
print(len(siblinglist))
for sibling in siblinglist:
    x = re.findall("^.*\.", sibling.get_attribute('id'))[0]
    xpathstring = '//div[starts-with(@id, "{0}")]'.format(x)
    childlist = driver.find_elements_by_xpath(xpathstring)
    print("siblings", sibling.get_attribute('id'))
    print(len(childlist))
    for child in childlist:
        print("childs are :" + child.get_attribute('id'))

## ACCESS Table
# //*[@id='large-table']//th //*[@id='large-table']/tbody/tr //*[@id="large-table"]/tbody/tr[1]/td[1]
rowlist = driver.find_elements_by_xpath('//*[@id="large-table"]/tbody/tr')

print('Total no of rows : ' +str(len(rowlist)))
for row in rowlist:
    y = row.get_attribute('class')
    xpathstring1 = '//*[@id="large-table"]/tbody//*[@class="{0}"]/td'.format(y)
    columnlist = driver.find_elements_by_xpath(xpathstring1)
    print('Total no of columns in row : ' +str(len(columnlist)))
    for column in columnlist:
        print('data in : ' +column.text)
      
driver.quit()
