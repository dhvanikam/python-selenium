from selenium import webdriver
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

options = webdriver.ChromeOptions()
prefs =  {"download.default_directory" : "/Users/dhvani/Downloads/Test"}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=options)

driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
link = driver.find_element_by_link_text('File Download')
link.click()
print(driver.current_url)

FileCount = 0
Filelist = driver.find_elements_by_xpath('//*[@class="example"]//a[@href]')
print(len(Filelist))
for file in Filelist:
    print(file.text)
    link = driver.find_element_by_link_text(file.text)
    link.click()
driver.quit()