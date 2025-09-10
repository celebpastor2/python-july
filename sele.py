from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOption
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By#tool to help in selection of elements withi our page
from selenium.webdriver.support.ui import WebDriverWait #wait unntil a particular element is visible on the page
from selenium.webdriver.support import expected_conditions as EC#desgin a conditio for your web drive to wait
from webdriver_manager.chrome   import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains

option = Options()

#adding browser settings
option.add_argument("--headless")
option.add_argument("--disable-gpu")
option.add_argument("--window-size=1920x700")
option.add_argument("--incognito")
option.add_argument("--user-agent=string")
option.add_argument("--disable-notification")
#option.add_argument("--disable-extensions")
#option.add_extension("extension.crx")


chrome = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=option
)

foption = FirefoxOption()
#foption.add_argument("--headless")
#foption.add_argument("--width=30px")
#foption.add_argument("--height=30px")

firefox = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=foption
)

chrome.get("https://facebook.com")
firefox.get("https://facebook.com")

print("chrome title", chrome.title)
print("firefox title", firefox.title)

element = WebDriverWait(firefox, 10).until(EC.presence_of_element_located((By.ID, "email")))
element.send_keys("samuelphillip@gmail.com")

element = chrome.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[7]/section")

#chain finding
products = element.find_elements(By.CSS_SELECTOR, "img")
element.click()
element.send_keys("value")#helps to fill form
element.clear()
element.get_attribute("name")
element.screenshot("filename.png")
element.submit()

#advanced interaction on the page with selenium
action  = ActionChains(chrome)
action.move_to_element(element).pause(3).click(element).pause(3).send_keys("value").pause(2).perform()
action.double_click(element).perform()
action.context_click(element).perform()





#A webelement Object is a representation of an html element within you selenium web browser



chrome.quit()
firefox.quit()

