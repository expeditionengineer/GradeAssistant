from time import sleep
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    """Function to test the login functionality of the website

    The story of the test is as follows: The user `admin` visits the website, logs in 
    and checks his(her dashboard. The dashboard should contain at least one class Element, which should be clickable.
    If the class is clicked the user is redirected to the Class-Page, which contains a list of all students and their grades.

    """
    driver = webdriver.Firefox()  # or webdriver.Chrome(), depending on your browser
    # driver.implicitly_wait(5)
    
    driver.get("http://localhost:3000")
    
    wait = WebDriverWait(driver, 5)  # wait up to 10 seconds
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
    try:
        classBoxes = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "classBox")))
    
    except:
        resfreshButton = driver.find_element(By.XPATH, "//button[@id='refresh']")
        resfreshButton.click()
        classBoxes = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "classBox"))) 
        classBoxes = driver.find_elements(By.CLASS_NAME, "classBox")   
    
    assert len(classBoxes) > 0, "No divs with class 'classBox' found"
    
    classBox = random.choice(classBoxes)
    classBox.click()

    # on the webpage of the class, there should be a list of students with their grades:
    students = driver.find_elements(By.CLASS_NAME, "student")

    assert len(students) > 0, "No students found on class page"

    driver.quit()

test_login()