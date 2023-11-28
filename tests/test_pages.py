from selenium.webdriver.common.by import By


def test_main_page(browser):
    browser.get("http://192.168.1.240:8081")
    assert browser.title == "Your Store"
    wish_list = browser.find_element(By.CSS_SELECTOR, "#wishlist-total")
    assert wish_list.text == "Wish List (0)"
    cart = browser.find_element(By.CSS_SELECTOR, "#cart-total")
    assert cart.text == "0 item(s) - $0.00"
    link = browser.find_element(By.LINK_TEXT, "Checkout")
    assert link.is_displayed() is True
    search = browser.find_element(By.CSS_SELECTOR, ".col-sm-5")
    assert search.is_displayed() is True


def test_catalog_page(browser):
    browser.get("http://192.168.1.240:8081/desktops")
    assert browser.title == "Desktops"
    title = browser.find_element(By.CSS_SELECTOR, "h2")
    assert title.text == "Desktops"
    title_2 = browser.find_element(By.CSS_SELECTOR, "h3")
    assert title_2.text == "Refine Search"
    compare = browser.find_element(By.CSS_SELECTOR, "#compare-total")
    assert compare.text == "Product Compare (0)"
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default.active")
    assert button.is_enabled() is True


def test_product_page(browser):
    browser.get("http://192.168.1.240:8081/desktops/test")
    assert browser.title == "Apple Cinema 30"
    title = browser.find_element(By.CSS_SELECTOR, "h1")
    assert title.text == 'Apple Cinema 30"'
    cart_button = browser.find_element(By.CSS_SELECTOR, "#button-cart")
    assert cart_button.text == "Add to Cart"
    button = browser.find_element(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    assert button.is_displayed() is True
    select_tab = browser.find_element(By.CSS_SELECTOR, "[value='4']")
    assert select_tab.is_selected() is False


def test_admin_page(browser):
    browser.get("http://192.168.1.240:8081/admin")
    assert browser.title == "Administration"
    title = browser.find_element(By.CSS_SELECTOR, ".panel-title")
    assert title.text == "Please enter your login details."
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    assert button.is_displayed() is True
    assert button.text == "Login"
    button.click()
    alert = browser.find_element(By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    assert alert.text == "No match for Username and/or Password.\n×"


def test_register_page(browser):
    browser.get("http://192.168.1.240:8081/index.php?route=account/register")
    assert browser.title == "Register Account"
    input = browser.find_element(By.CSS_SELECTOR, "#input-firstname")
    assert input.is_displayed() is True
    checkbox = browser.find_element(By.CSS_SELECTOR, "[name = 'agree']")
    assert checkbox.is_selected() is False
    checkbox.click()
    assert checkbox.is_selected() is True
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    assert button.get_property("value") == "Continue"
