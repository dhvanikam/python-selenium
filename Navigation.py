from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
print(driver.current_url)

link = driver.find_element_by_link_text('A/B Testing')
link.click()
print(driver.current_url)

sub_link = driver.find_element_by_link_text('Elemental Selenium')
sub_link.click()
print(sub_link.text)
print(driver.current_url)

driver.quit()