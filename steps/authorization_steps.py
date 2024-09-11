import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@given('я открываю страницу авторизации')
def step_open_authorization_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://127.0.0.1:5000/authorization")

@when('я ввожу логин "{username}" и пароль "{password}"')
def authorization_valid(context, username, password):
    context.driver.find_element(By.NAME, "Login").clear()
    context.driver.find_element(By.NAME, "Login").send_keys(username)
    context.driver.find_element(By.NAME, "Password").clear()
    context.driver.find_element(By.NAME, "Password").send_keys(password)

@when('отправляю форму авторизации')
def step_submit_authorization_form(context):
    context.driver.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(1)

@then('авторизация должна пройти успешно')
def step_check_successful_login(context):
    success_message_locator = (By.XPATH, "//div[contains(., 'Вы успешно авторизовались')]")

    try:
        WebDriverWait(context.driver, 10).until(EC.presence_of_element_located(success_message_locator))
    except TimeoutException:
        print("TimeoutException occurred. Page HTML:")
        print(context.driver.page_source)
        raise
    
    success_message_element = context.driver.find_element(*success_message_locator)
    assert success_message_element.is_displayed(), "Successful login message not found"

    context.driver.quit()