import pytest
from pageobjects.AT_LoginPage import ATLogin_page
from utilities.Logger import Loggen
import allure
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures("setup")
class Test_ATLogin:
    log = Loggen.read_logger()

    @pytest.mark.ddtparams
    def test_login_TC01(self, setup, DataForLogin):
        self.log.info("Test Case test_login_TC01 Started")
        self.log.info("Opening Browser and Navigating to AT Login Page")
        self.driver = setup
        lp = ATLogin_page(self.driver)

        TestCase_Status_List = []

        username = DataForLogin[0]
        password = DataForLogin[1]

        self.log.info("Entering Username")
        lp.Enter_Username(username)
        self.log.info("Entering Username")
        lp.Enter_Password(password)
        self.log.info("Clicking Login Button")
        lp.Click_Login_Button()
        self.log.info("Validating Login Status")
        lp.ValidateLoginStatus()

        Expected_Result = DataForLogin[2]
        Actual_Result = lp.ValidateLoginStatus()

        if Expected_Result == "Pass" and Actual_Result == "Pass":
            self.log.info("Updating TestCase_Status_List as Pass")
            TestCase_Status_List.append("PASS")
            self.log.info("Taking Pass Screenshot")
            self.driver.save_screenshot(
                "C:\\Users\\aksha\\PycharmProjects\\PythonProject1\\Screenshots\\test_login_TC01_PASS.png")
            self.log.info("Test Case test_login_TC01 PASSED")
            self.log.info("Taking Allure Pass Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_TC01_PASS",
                          attachment_type=AttachmentType.PNG)

        elif Expected_Result == "Fail" and Actual_Result == "Fail":
            self.log.info("Updating TestCase_Status_List as Pass")
            TestCase_Status_List.append("PASS")
            self.log.info("Taking Fail Screenshot")
            self.driver.save_screenshot(
                "C:\\Users\\aksha\\PycharmProjects\\PythonProject1\\Screenshots\\test_login_TC01_FAIL.png")
            self.log.info("Test Case test_login_TC01 PASSED")
            self.log.info("Taking Allure Fail Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_TC01_Fail",
                          attachment_type=AttachmentType.PNG)

        else:
            self.log.info("Updating TestCase_Status_List as Pass")
            TestCase_Status_List.append("FAIL")
            self.log.info("Taking Fail Screenshot")
            self.driver.save_screenshot(
                "C:\\Users\\aksha\\PycharmProjects\\PythonProject1\\Screenshots\\test_login_TC01_FAIL.png")
            self.log.info("Test Case test_login_TC01 FAILED")
            self.log.info("Taking Allure Fail Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_TC01_Fail",
                          attachment_type=AttachmentType.PNG)

        assert "Fail" not in TestCase_Status_List
        self.log.info("TestCase_Status_List " + str(TestCase_Status_List))
        self.log.info("Test Case test_login_TC01 Completed")
