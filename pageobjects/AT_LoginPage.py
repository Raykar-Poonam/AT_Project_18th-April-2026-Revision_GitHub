from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ATLogin_page:
    Input_Username_ID = "username"
    Input_Password_ID = "password"
    Button_Login_NAME = "login"
    Validate_LoginStatus_XPATH = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Username(self, username):
        self.driver.find_element(By.ID, self.Input_Username_ID).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.ID, self.Input_Password_ID).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(By.NAME, self.Button_Login_NAME).click()

    def ValidateLoginStatus(self):

        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.Validate_LoginStatus_XPATH)))
            # self.driver.find_element(By.XPATH, self.Validate_LoginStatus_XPATH)
            return "Pass"

        except:
            return "Fail"
