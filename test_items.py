import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Проверяем, что на странице есть кнопка "Добавить в корзину" на нужном языке
def test_item_page_has_add_to_cart_button(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Язык, который мы передали в командной строке
    user_language = browser.execute_script("return navigator.language || navigator.userLanguage;")

    # Ожидаем появление кнопки добавления в корзину
    try:
        add_to_cart_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
        )
    except Exception as e:
        pytest.fail(f"Кнопка 'Добавить в корзину' не найдена: {e}")

    # Получаем текст кнопки
    button_text = add_to_cart_button.text.strip()

    # Словарь с ожидаемыми текстами для разных языков
    expected_texts = {
        "en": "Add to basket",
        "es": "Añadir al carrito",
        "fr": "Ajouter au panier",
        "de": "In den Warenkorb",
        "ru": "Добавить в корзину",
        "it": "Aggiungi al carrello",
        "pl": "Dodaj do koszyka",
        "pt": "Adicionar ao carrinho"
    }

    # Проверяем, что текст кнопки соответствует ожидаемому для выбранного языка
    expected_text = expected_texts.get(user_language[:2], None)
    if not expected_text:
        pytest.fail(f"Неизвестный язык: {user_language}. Поддерживаемые: {list(expected_texts.keys())}")

    assert expected_text in button_text, \
        f"Ожидалось '{expected_text}', но получено: '{button_text}'"

    print(f"✅ Кнопка содержит текст на языке '{user_language}': '{button_text}'")