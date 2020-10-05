import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://orteil.dashnet.org/cookieclicker")
print(driver.title)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]


actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = cookie_count.text
    print(count)