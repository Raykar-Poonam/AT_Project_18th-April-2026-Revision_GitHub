import pytest
from pageobjects.AT_LoginPage import ATLogin_page
from utilities.ReadconfigFile import Readconfig
from utilities.Logger import Loggen


@pytest.mark.usefixtures("setup")
class Test_ATLogin:
    log = Loggen.read_logger()

    @pytest.mark.general
    def test_login_TC01(self, setup):
        self.log.info("Test Case test_login_TC01 Started")
        self.log.info("Opening Browser and Navigating to AT Login Page")
        self.driver = setup
        lp = ATLogin_page(self.driver)

        username = Readconfig.getUsername()
        password = Readconfig.getPasssword()

        self.log.info("Entering Username")
        lp.Enter_Username(username)
        self.log.info("Entering Username")
        lp.Enter_Password(password)
        self.log.info("Clicking Login Button")
        lp.Click_Login_Button()
        self.log.info("Validating Login Status")
        lp.ValidateLoginStatus()

        if lp.ValidateLoginStatus() == "Pass":
            self.log.info("Login Status Validation Passed")
            self.log.info("Taking Pass Screenshot")
            self.driver.save_screenshot(
                "C:\\Users\\aksha\\PycharmProjects\\PythonProject1\\Screenshots\\test_login_TC01_PASS.png")
            self.log.info("Test Case test_login_TC01 PASSED")
            assert True

        else:
            self.log.info("Login Status Validation Failed")
            self.log.info("Taking Fail Screenshot")
            self.log.info("Test Case test_login_TC01 FAILED")
            self.driver.save_screenshot(
                "C:\\Users\\aksha\\PycharmProjects\\PythonProject1\\Screenshots\\test_login_TC01_FAIL.png")
            assert False

        self.log.info("Test Case test_login_TC01 Completed")