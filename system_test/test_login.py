from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    driver = webdriver.Firefox()  # or webdriver.Chrome(), depending on your browser
    # driver.implicitly_wait(5)
    
    driver.get("http://localhost:3000")
    
    wait = WebDriverWait(driver, 10)  # wait up to 10 seconds
    usernameField = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']")))
    # breakpoint()
    passwordField = driver.find_element(By.XPATH, "//input[@id='password']")
    
    usernameField.send_keys("admin")
    passwordField.send_keys("hallo12345")

    login_button = driver.find_element(By.XPATH, "//button[@id='submit']")
    login_button.click()
    
    # assert driver.current_url == "http://localhost:3000/dashboard"
    
    # class_boxes = driver.find_elements_by_class_name("classBox")
    # breakpoint()
    class_boxes = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "classBox")))
    
    assert len(class_boxes) > 0, "No divs with class 'classBox' found"

    driver.quit()

test_login()