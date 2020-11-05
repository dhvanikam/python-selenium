from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
Home_URL = driver.current_url

link = driver.find_element_by_link_text('Disappearing Elements')
link.click()
print(driver.current_url)


# AllElements = driver.find_elements_by_tag_name('a')
# for element in AllElements:
#     print(element.text)
    
def Reload():
    driver.get("http://the-internet.herokuapp.com/")
    link = driver.find_element_by_link_text('Disappearing Elements')
    link.click()

#Home Link
try:
    Home = driver.find_element_by_link_text('Home')
    if Home.is_displayed():
        Home.click()
        Current_URL = driver.current_url
        if Home_URL == Current_URL :
            print('We are at home page')
        else:
            print('Wrong page')
except NoSuchElementException:
    print('About Element not present')


#About Link
Reload()
try:
    About = driver.find_element_by_link_text('About')
    if About.is_displayed():
        About.click()
        print(driver.current_url)
except NoSuchElementException:
    print('About Element not present')


#Contact Us Link
Reload()
try:
    ContactUs = driver.find_element_by_link_text('Contact Us')
    if ContactUs.is_displayed():
        ContactUs.click()
        print(driver.current_url)
except NoSuchElementException:
    print('ContactUs Element not present')


# Portfolio Link
Reload()
try:
    Portfolio = driver.find_element_by_link_text('Portfolio')
    if Portfolio.is_displayed():
        Portfolio.click()
        print(driver.current_url)
except NoSuchElementException:
    print('Portfolio Element not present')

# Gallery Link
Reload()
try:
    Gallery = driver.find_element_by_link_text('Gallery')
    if Gallery.is_displayed():
        Gallery.click()
        print(driver.current_url)
except NoSuchElementException:
    print('Gallery Element not present')


driver.quit()