from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path=r"C:\chromedrive\chromedriver.exe", options=options)

url = "http://158.69.76.135/level2.php"

my_id = "9"

for i in range(3):
	driver.get(url)
	formulario = driver.find_element_by_name('id')
	submit = driver.find_element_by_name('holdthedoor')
	formulario.send_keys(my_id)
	submit.click()
driver.close()
