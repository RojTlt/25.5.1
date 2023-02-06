import pytest
from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_show_page_my_pets():
   '''Проверяет, что мы оказались на странице "Мои питомцы".'''

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   pytest.driver.find_element_by_id('email').send_keys(valid_email)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   pytest.driver.find_element_by_id('pass').send_keys(valid_password)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
   pytest.driver.find_element_by_link_text("Мои питомцы").click()


   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets/'