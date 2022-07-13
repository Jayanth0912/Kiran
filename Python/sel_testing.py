from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\gopat\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
config = {
    # "url":"http://www.python.org"
    "url":"http://www.svist.org"
}
driver.get(config.get("url"))
but = driver.find_element(By.XPATH,"//*[@id='myTopnav']/a[7]")
but.click()
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME,"q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# # elem.send_keys(Keys.F5)
# assert "No results found." not in driver.page_source
import time
time.sleep(2)
driver.close()