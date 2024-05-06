from selenium import webdriver
import time
# from selenium.webdriver.common.keys import Keys

def get_driver():
    options = webdriver.EdgeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Edge()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    return driver

def main():
    driver=get_driver()
    driver.find_element(by="id",value="username").send_keys("student")
    time.sleep(2)
    driver.find_element(by="id",value="password").send_keys("Password123")
    time.sleep(2)
    driver.find_element(by="id",value="submit").click()
    time.sleep(8)

main()