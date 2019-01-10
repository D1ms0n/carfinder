from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

# self.driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')
#driver = webdriver.Chrome()
driver.get("http://192.168.1.229:8000")

print(driver.title)