import os

import allure
from selene import browser, have
from selene.support.shared.jquery_style import s, ss
import time
import requests
from allure_commons._allure import step
from dotenv import load_dotenv

from tests.conftest import BASE_URL
from utils.utils import post_request


@allure.title(
    "Аuthorization and adding an item to the shopping cart with the parameters specified"
)
@allure.feature("Basket functionality")
@allure.story("adding and removing products")
@allure.label('type', 'regression')
@allure.tag('UI', 'API')
@allure.severity('critical')
@allure.label("owner", "Davydov")
def test_add_product_to_cart_with_params():
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    responce = requests.post(
        BASE_URL + "login",
        data={'Email': login, 'Password': password, 'RememberMe': True},
        allow_redirects=False,
    )
    assert responce.status_code == 302
    cookie = responce.cookies.get("NOPCOMMERCE.AUTH")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    responce_2 = requests.post(
        BASE_URL + "addproducttocart/details/74/1",
        data={
            "product_attribute_74_5_26": 82,
            "product_attribute_74_6_27": 85,
            "product_attribute_74_3_28": 87,
            "product_attribute_74_8_29": 90,
            "addtocart_74.EnteredQuantity": 1,
        },
        allow_redirects=False,
        cookies={"NOPCOMMERCE.AUTH": cookie},
    )
    assert responce_2.status_code == 200
    with step(
        "1. 'API'. Authorization on the website and adding the product to the cart"
    ):
        browser.open(BASE_URL)
        browser.open(f"{BASE_URL}cart")
    with step(
        "2. 'UI'. Сhecking the product in the cart and removing it from the cart"
    ):
        s('.product-name').should(have.text('Build your own expensive computer'))
        s('.remove-from-cart').click()
        s('.update-cart-button').press_enter()


@allure.title(
    "Authorization and adding an item to the shopping cart without parameters"
)
@allure.feature("Basket functionality")
@allure.story("adding and removing products")
@allure.label('type', 'regression')
@allure.tag('UI', 'API')
@allure.severity('critical')
@allure.label("owner", "Davydov")
def test_add_product_to_cart_without_params():
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    response = post_request(
        "login", data={"Email": login, "Password": password}, allow_redirects=False
    )
    cookies = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
    response_2 = post_request(
        "addproducttocart/catalog/31/1/1", cookies={"NOPCOMMERCE.AUTH": cookies}
    )
    assert response_2.status_code == 200
    browser.open(BASE_URL)
    browser.open(f"{BASE_URL}cart")
    browser.element('.product-name').should(have.text("14.1-inch Laptop"))
    browser.element(".remove-from-cart").click()
    browser.element(".update-cart-button").press_enter()
