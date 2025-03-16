import pytest
from .pages.product_page import ProductPage


@pytest.mark.skip
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


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.should_not_be_success_message_not_element_present()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_not_element_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.should_not_be_success_message_disappeared()
