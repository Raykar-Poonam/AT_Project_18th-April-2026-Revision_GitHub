import pytest
from selenium import webdriver

@pytest.fixture()
def setup():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practice.automationtesting.in/my-account/")

    yield driver
    driver.quit()




@pytest.fixture(params=[("poonamraykar89@gmail.com","Poonamraykar@1992","Pass"),
                        ("poonamraykar89@gmail.com1","Poonamraykar@1992","Fail"),
                        ("poonamraykar89@gmail.com","Poonamraykar@19921","Fail"),
                        ("poonamraykar89@gmail.com1","Poonamraykar@19921","Fail")
                        ])

def DataForLogin(request):
    return request.param

