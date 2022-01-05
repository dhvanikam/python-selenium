from seleniumwire import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

capabilities = DesiredCapabilities.CHROME
# capabilities["loggingPrefs"] = {"performance": "ALL"}  # chromedriver < ~75
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}  # chromedriver 75+

driver = webdriver.Chrome(
    r"chromedriver",
    desired_capabilities=capabilities,
)
driver.get("http://the-internet.herokuapp.com/")

link = driver.find_element_by_link_text('Broken Images')
link.click()
print(driver.current_url)

InvalidImageCount = 0
imagelist = driver.find_elements_by_tag_name('img')
print('Total number of images are : ' + str(len(imagelist)))

for element in imagelist:
    src = element.get_attribute('src')
    print(src)
    for request in driver.requests:
        if request.url == src and request.response.status_code == 404:
            InvalidImageCount += 1
            print("image is broken\n")
        elif request.url == src and request.response.status_code == 200:
            print("image is OK\n")


print('Total invalid images are ' + str(InvalidImageCount))
driver.quit()


