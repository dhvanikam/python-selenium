from seleniumwire import webdriver
from selenium.webdriver.remote.webelement import WebElement
from http.client import HTTPResponse
import logging
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


capabilities = DesiredCapabilities.CHROME
# capabilities["loggingPrefs"] = {"performance": "ALL"}  # chromedriver < ~75
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}  # chromedriver 75+

driver = webdriver.Chrome(
    r"chromedriver",
    desired_capabilities=capabilities,
)
driver.get("https://github.com/saucelabs/the-internet")

link = driver.find_element_by_link_text('Broken Images')
link.click()
print(driver.current_url)


# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        print(
            request.url,
            request.response.status_code,
            request.response.headers['Content-Type']
        )

#driver.get('http://the-internet.herokuapp.com/asdf.jpg')
#driver.get('http://the-internet.herokuapp.com/img/avatar-blank.jpg')
# Imglink = driver.find_element_by_xpath('/html/body/div[2]/div/div/img[1]')
# Imglink.click()
# print(str(driver.get_log('browser')))
#print(str(driver.get_log('server')))
# print(str(driver.get_log('performance')))
for line in driver.get_log('performance'):
    f = open("log.txt", "wt")
    f.write(str(line))
    f.close()
#(404..Not.Found.)+
#line_regex = re.compile(/(404..Not.Found.)+/)

with open("log.txt", "r") as in_file:
    # Loop over each log line
    for line in in_file:
        # If log line matches our regex, print to console, and output file
        if (re.search("(404..Not.Found.)+",line)):
            print('found match')
            print(line)
        else: 
            print('No match')

driver.quit()
# InvalidImageCount = 0
# #imagelist = []
# imagelist = driver.find_elements_by_tag_name('img')
# print('Total number of images are : ' + str(len(imagelist)))

# for e in imagelist:
#     if (e is None):
#         verifyimgActive(e)
# print()

# #def verifyimgActive(element):
#  #   client.

