from selenium import webdriver
import warnings
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.keys import Keys

warnings.filterwarnings("ignore", category=DeprecationWarning)

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
link = driver.find_element_by_link_text('File Upload')
link.click()
print(driver.current_url)
try:
    Choose_file = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/input[1]')
    Choose_file.send_keys("/Users/dhvani/Downloads/Test/some-file.txt")
    uploadbutton = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/input[2]')
    uploadbutton.click()
    file_upload_success = driver.find_element_by_xpath('/html/body/div[2]/div/div/div')
    print(file_upload_success.text)
except InvalidArgumentException as exception:
    print('File not found to upload')
driver.quit()