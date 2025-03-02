import time
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_name = page.product_name()  # получаем имя товара на странице
    product_value = page.product_value()  # получаем цену товара на странице
    page.add_to_card()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # решаем задачу в alert
    page.product_in_cart(product_name)  # проверяем имя товара в корзине
    page.value_in_cart(product_value)  # проверяем цену товара в корзине
