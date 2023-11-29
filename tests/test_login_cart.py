from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(browser):
    browser.get("http://192.168.1.240:8081/admin")
    name_field = browser.find_element(By.CSS_SELECTOR, "#input-username")
    name_field.click()
    name_field.send_keys("user")
    surname_field = browser.find_element(By.CSS_SELECTOR, "#input-password")
    surname_field.click()
    surname_field.send_keys("bitnami")
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".hidden-xs.hidden-sm.hidden-md")))
    button_logout = browser.find_element(By.CSS_SELECTOR, ".hidden-xs.hidden-sm.hidden-md")
    assert button_logout.text == "Logout"


def test_add_product_in_cart(browser):
    browser.get("http://192.168.1.240:8081")
    cart = browser.find_element(By.CSS_SELECTOR, "#cart-total")
    assert cart.text == "0 item(s) - $0.00"
    browser.find_element(By.CSS_SELECTOR, ".col-sm-12 .row .product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(1) .button-group button:nth-child(1)").click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart-total")))
    cart = browser.find_element(By.CSS_SELECTOR, "#cart-total")
    assert cart.text == "1 item(s) - $602.00"


def test_change_currency_on_main_page(browser):
    browser.get("http://192.168.1.240:8081")
    price = browser.find_element(By.CSS_SELECTOR, ".col-sm-12 .row .product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(1) .caption .price")
    assert price.text == "$602.00\nEx Tax: $500.00"
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle").click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='EUR']"))).click()
    price = browser.find_element(By.CSS_SELECTOR, ".col-sm-12 .row .product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(1) .caption .price")
    assert price.text == "472.33€\nEx Tax: 392.30€"


def test_change_currency_on_product_page(browser):
    browser.get("http://192.168.1.240:8081/desktops")
    price = browser.find_element(By.CSS_SELECTOR, "#product-category .product-layout.product-grid.col-lg-4.col-md-4.col-sm-6.col-xs-12:nth-child(3) .price")
    assert price.text == "$122.00\nEx Tax: $100.00"
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle").click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='EUR']"))).click()
    price = browser.find_element(By.CSS_SELECTOR, "#product-category .product-layout.product-grid.col-lg-4.col-md-4.col-sm-6.col-xs-12:nth-child(3) .price")
    assert price.text == "95.72€\nEx Tax: 78.46€"
