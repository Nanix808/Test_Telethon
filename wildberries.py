from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def parse_wildberries(goods: str):
    url = f"https://www.wildberries.ru/catalog/0/search.aspx?search={goods}"  # URL сайта Wildberries

    # Initialize the Remote WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub", options=chrome_options
    )
    browser.get(url)

    WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='product-card__wrapper']")
        )
    )
    # получаем все линки
    link_list = browser.find_elements(
        By.XPATH,
        "//a[@class='product-card__link j-card-link j-open-full-product-card']",
    )
    goods_list = []
    for i, link in enumerate(link_list):
        goods_list.append(
            {i: [link.get_attribute("aria-label"), link.get_attribute("href")]}
        )
    return goods_list[:10]
