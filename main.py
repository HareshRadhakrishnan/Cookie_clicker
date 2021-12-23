from selenium import webdriver
from time import time

timeout = 10


driver = webdriver.Chrome("C:/Users/Haresh/PycharmProjects/chromedriver_win32/chromedriver.exe")

driver.get("https://orteil.dashnet.org/cookieclicker/")

btn_cookie = driver.find_element_by_xpath('//*[@id="bigCookie"]')

game_over = False
Should_end = time() + 60*5

while not game_over:
    time_start = time()
    while time() < time_start + timeout:
        btn_cookie.click()
        if time() > Should_end:
            game_over = True
        elif time() > time_start + 5:
            time_start = time()

            products = driver.find_elements_by_css_selector('div[class*="unlocked"]')
            for num in range(0, len(products)):
                price = products[num].find_element_by_css_selector(f'[id*="productPrice{num}"]')
                if num == len(products)-1:
                    products[num].click()


cookies = driver.find_element_by_css_selector('[id*="cookies"]').text
cookies = cookies.split(":")[1]
print(f"Cookie/second : {cookies}")

# driver.close()