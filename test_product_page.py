import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo', ["0", "1", "2", "3", "4", "5", "6",
                                   pytest.param("7", marks=pytest.mark.xfail),
                                   "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    product_name = page.product_name()  # получаем имя товара на странице
    product_value = page.product_value()  # получаем цену товара на странице
    page.add_to_card()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # решаем задачу в alert
    page.product_in_cart(product_name)  # проверяем имя товара в корзине
    page.value_in_cart(product_value)  # проверяем цену товара в корзине
