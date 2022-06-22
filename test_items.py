from selenium.webdriver.common.by import By


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    element1 = browser.find_elements(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert len(element1) > 0, 'Button not found' 
