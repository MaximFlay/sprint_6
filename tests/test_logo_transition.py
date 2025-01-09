import allure

from conftest import driver
from pages.main_page import MainPage


class TestLogoTransition:
    @allure.title('Проверка перехода на главную страницу при клике на лого "Самокат" в шапке')
    def test_logo_transition_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_transition_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        main_page.wait_url_until_not_about_blank()
        current_url = main_page.current_url()
        assert ('ya.ru' in current_url) or ('dzen.ru' in current_url) or ('yandex.ru' in current_url)