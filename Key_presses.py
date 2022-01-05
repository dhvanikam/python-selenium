from selenium import webdriver
import warnings
from selenium.webdriver.common.keys import Keys
import time

warnings.filterwarnings("ignore", category=DeprecationWarning)

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
link = driver.find_element_by_link_text('Key Presses')
link.click()
print(driver.current_url)
Keylist = [Keys.ADD,Keys.ARROW_DOWN,Keys.ARROW_LEFT,Keys.ARROW_RIGHT,Keys.ARROW_UP,Keys.BACK_SPACE,Keys.CANCEL,Keys.COMMAND,Keys.CONTROL,Keys.DELETE,Keys.ALT,Keys.DECIMAL,Keys.DIVIDE,Keys.DOWN,Keys.END,Keys.ENTER,Keys.EQUALS,Keys.ESCAPE,Keys.F1,Keys.F2,Keys.F3,Keys.F4,Keys.F5,Keys.F6,Keys.F7,Keys.F8,Keys.F9,Keys.F10,Keys.F11,Keys.F12,Keys.LEFT,Keys.MULTIPLY,Keys.NUMPAD0,Keys.NUMPAD2,Keys.NUMPAD3,Keys.NUMPAD4,Keys.NUMPAD5,Keys.NUMPAD6,Keys.NUMPAD7,Keys.NUMPAD8,Keys.NUMPAD9,Keys.PAGE_DOWN,Keys.PAGE_UP,Keys.RETURN,Keys.PAUSE,Keys.RIGHT,Keys.SEMICOLON,Keys.SUBTRACT,Keys.SHIFT,Keys.SPACE,Keys.TAB,Keys.UP]

for key in Keylist:
    input = driver.find_element_by_id('target')
    input.send_keys(key)
    result = driver.find_element_by_xpath('//*[@id="result"]')
    print(result.text)
    time.sleep(1)
driver.quit()