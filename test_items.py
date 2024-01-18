import time
from selenium.webdriver.common.by import By

class TestFindButton():
    def test_find_bucket_button(self, browser):
        browser.get("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        assert len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")) == 1, "Кнопка добавления в корзину отсутствует"


