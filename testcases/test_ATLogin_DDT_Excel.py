import pytest
from selenium import webdriver

from pageobjects.AT_LoginPage import ATLogin_page
from utilities.Logger import Loggen
import allure
from allure_commons.types import AttachmentType
from utilities import ExcelMethods


@pytest.mark.usefixtures("setup")
class Test_ATLogin:
    log = Loggen.read_logger()
    Excel_Path = "C:\\Users\\aksha\\PycharmProjects\\PythonProject1\\testcases\\Test Data\\Testcase_001.xlsx"

    @pytest.mark.ddtexcel
    def test_login_TC01(self):

        row_no = ExcelMethods.row_num(self.Excel_Path, "Sheet1")
        print("row_no: ",row_no)

        TestCase_Status_List = []

        for r in range(2, row_no + 1):

            self.log.info("Test Case test_login_TC01 Started")
            self.log.info("Opening Browser and Navigating to AT Login Page")
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get("https://practice.automationtesting.in/my-account/")
            # self.driver.implicitly_wait(10)
            lp = ATLogin_page(self.driver)

            username = ExcelMethods.readData(self.Excel_Path, "Sheet1", r, 2)
            password = ExcelMethods.readData(self.Excel_Path, "Sheet1", r, 3)

            self.log.info("Entering Username for row = " + str(r))
            lp.Enter_Username(username)
            self.log.info("Entering Password for row = " + str(r))
            lp.Enter_Password(password)
            self.log.info("Clicking Login Button for row = " + str(r))
            lp.Click_Login_Button()
            self.log.info("Validating Login Status for row = " + str(r))
            # lp.ValidateLoginStatus()

            Expected_Result = ExcelMethods.readData(self.Excel_Path, "Sheet1", r, 4)
            Actual_Result = lp.ValidateLoginStatus()

            if Expected_Result == "Pass" and Actual_Result == "Pass":

                self.log.info("Updating TestCase_Status_List as Pass for row = " + str(r))
                TestCase_Status_List.append("PASS")
                ExcelMethods.writeData(self.Excel_Path, "Sheet1", r, 5, "Pass")
                self.log.info("Taking Pass Screenshot for row = " + str(r))
                self.driver.save_screenshot(
                    f"C:\\Users\\aksha\\PycharmProjects\\PythonProject1\\Screenshots\\test_login_TC01_PASS_for row {r}.png")
                self.log.info("Test Case test_login_TC01 PASSED for row = " + str(r))
                self.log.info("Taking Allure Pass Screenshot for row = " + str(r))
                allure.attach(self.driver.get_screenshot_as_png(), name="test_login_TC01_PASS for row = " + str(r),
                              attachment_type=AttachmentType.PNG)


            elif Expected_Result == "Fail" and Actual_Result == "Fail":
                self.log.info("Updating TestCase_Status_List as Pass for row = " + str(r))
                TestCase_Status_List.append("PASS")
                ExcelMethods.writeData(self.Excel_Path, "Sheet1", r, 5, "Fail")
                self.log.info("Taking Fail Screenshot for row = " + str(r))
                self.driver.save_screenshot(
                    f"C:\\Users\\aksha\\PycharmProjects\\PythonProject1\\Screenshots\\test_login_TC01_PASS_for row {r}.png")
                self.log.info("Test Case test_login_TC01 PASSED for row = " + str(r))
                self.log.info("Taking Allure Fail Screenshot for row = " + str(r))
                allure.attach(self.driver.get_screenshot_as_png(), name="test_login_TC01_Fail for row = " + str(r),
                              attachment_type=AttachmentType.PNG)

            else:
                self.log.info("Updating TestCase_Status_List as Fail")
                TestCase_Status_List.append("FAIL")
                ExcelMethods.writeData(self.Excel_Path, "Sheet1", r, 5, "Fail")
                self.log.info("Taking Fail Screenshot for row = " + str(r))
                self.driver.save_screenshot(
                    f"C:\\Users\\aksha\\PycharmProjects\\PythonProject1\\Screenshots\\test_login_TC01_PASS_for row {r}.png")
                self.log.info("Test Case test_login_TC01 FAILED for row = " + str(r))
                self.log.info("Taking Allure Fail Screenshot for row = " + str(r))
                allure.attach(self.driver.get_screenshot_as_png(), name="test_login_TC01_Fail for row = " + str(r),
                              attachment_type=AttachmentType.PNG)
            self.log.info("Test Case test_login_TC01 Completed for row = " + str(r))
            self.driver.quit()

        assert "Fail" not in TestCase_Status_List
        self.log.info(f"Final Result: {TestCase_Status_List}")
