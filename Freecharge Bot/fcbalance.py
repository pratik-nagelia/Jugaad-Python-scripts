from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

with open('db.txt') as f:
    credentials = [x.strip().split(' : ') for x in f.readlines()]

url = 'https://www.freecharge.in/desktop/login'

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=options)
    # driver = webdriver.PhantomJS()
    # driver.maximize_window()
    driver.wait = WebDriverWait(driver, 5)
    return driver

def login(username , password):
    driver.get(url)
    email = driver.find_element_by_name("username")
    email.send_keys(username)
    passw = driver.find_element_by_name("password")
    passw.send_keys(password)
    sleep(1)
    passw.send_keys(Keys.RETURN)

def logout():
    button = driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div > header > div > div._2k4TI > div > div.PVUV4")))
    button.click()
    sleep(3)
    driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div > header > div > div._2k4TI > div > ul > li._3Xwim > a"))).click()
    sleep(2)

if __name__ == "__main__":
    counter = 0
    driver = init_driver()
    for username, password in credentials:
        counter += 1
        login(username, password)
        sleep(5)
        source = driver.find_element_by_css_selector("#app > div > div.container > div.right-bar > div > div._2z74u > div > div.j0-qi > span.eFrKl")
        print username + " = " + source.text
        logout()
        if (counter % 3 == 0):
            driver.quit()
            driver = init_driver()
    driver.quit()
