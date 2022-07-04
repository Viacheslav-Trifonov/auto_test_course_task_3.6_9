from selenium.webdriver.common.by import By
from conftest import link


def test_guest_should_see_login_link(browser):
    browser.get(link)
    element1 = browser.find_elements(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert len(element1) > 0, 'Button not found' 
