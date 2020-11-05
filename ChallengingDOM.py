from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import re


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")

link = driver.find_element_by_link_text('Challenging DOM')
link.click()
print(driver.current_url)

Button1 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/a[1]')
Button1.click()
hostDiv = driver.execute_script("return canvas;")
print(hostDiv)
Button1 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/a[1]')
print(Button1.text)
canvas = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/div/canvas')
canvas.click()
hostDiv = driver.execute_script("return canvas;")
print(hostDiv)
# canvas.screenshot('test1.png')
# img = cv2.imread('test1.png')
# text = pytesseract.image_to_string(img)
# print(text)


Button2 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/a[2]')
Button3 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/a[3]')

#Access table cells
# table_id = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/table/tbody')
# rows = table_id.find_elements_by_tag_name('tr')
# col = table_id.find_elements_by_tag_name('td')
# noOfRows = len(rows)
# print(noOfRows)
# rowno = 0 
# for row in rows:
#     columnno = 0 
#     col = row.find_elements_by_tag_name('td')
#     rowno += 1 
#     for column in col:
#         columnno += 1
#         print(column.text)
#         print("Cell Value Of row number " + str(rowno) + " and column number " + str(columnno) + " Is " + column.text)         
#     noOfColumns = len(col)
#     print(noOfColumns)

driver.quit()