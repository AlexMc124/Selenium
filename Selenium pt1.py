import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get("https://www.techwithtim.net")
print(driver.title)

# End of part 1
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
except:
    driver.quit()

print(main.text)