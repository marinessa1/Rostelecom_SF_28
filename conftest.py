
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome('/SF_module28_RT/chromedriver_mac_arm64/chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


