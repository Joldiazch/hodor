from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pytesseract

import numpy as np
import cv2

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path=r"C:\chromedrive\chromedriver.exe", options=options)

url = "http://158.69.76.135/level3.php"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r'-l eng --psm 4'
my_id = "1166"

for i in range(1024):
    driver.get(url)
    driver.execute_script("window.scrollTo(0, 135)")
    driver.save_screenshot("screenshot.png")
    formulario = driver.find_element_by_name('id')
    submit = driver.find_element_by_name('holdthedoor')
    in_captcha = driver.find_element_by_name('captcha')
    img = cv2.imread('screenshot.png', 0)
    captcha = img[580:, :70]
    text = pytesseract.image_to_string(captcha, config=custom_config)
    formulario.send_keys(my_id)
    in_captcha.send_keys(text)
    submit.click()
driver.close()
