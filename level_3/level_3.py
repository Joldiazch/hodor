from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



options = webdriver.ChromeOptions()
#options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path=r"C:\chromedrive\chromedriver.exe", options=options)

url = "http://158.69.76.135/level3.php"

driver.get(url)

images = driver.find_elements_by_tag_name('img')

src = images[1].get_attribute('src')
print(src)
driver.close()
