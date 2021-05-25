from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

option = Options()
option.headless = False
driver = webdriver.Chrome(executable_path=('C:\\webdrivers\\chromedriver.exe'),options=option)

username = input("Digite seu username")
password = input("Digite sua senha")

driver.get("https://www.instagram.com")
time.sleep(10)
driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
time.sleep(8)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password,  Keys.ENTER)
time.sleep(180)

driver.get("https://www.instagram.com/explore/tags/funnyvideos/")

print("Dormindo 10s")
time.sleep(3)
for i in range(1, 20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print(i)
    time.sleep(4)

posts = driver.find_elements_by_tag_name('a')

post = [elem.get_attribute('href') for elem in posts]


href = [href for href in post if '/p/' in href]
print(href)
print(str(len(posts)))


for i in href:
    driver.get(i)
    driver.execute_script("window.scrollTo(0, document.body.srollHeight);")
    try:
        driver.find_element_by_class_name('wpO6b ').click()
        time.sleep(15)
    except Exception as e:
        print("not like")
        time.sleep(5)



