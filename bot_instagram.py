from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

option = Options()
option.headless = False
driver = webdriver.Chrome(executable_path=('C:\\webdrivers\\chromedriver.exe'),options=option) #Coloque o caminho para o seu chromedriver.exe

username = input("Digite seu username")
password = input("Digite sua senha")

driver.get("https://www.instagram.com") # Selenium abrindo o site do instagram
time.sleep(10)
driver.find_element_by_xpath("//input[@name='username']").send_keys(username) # Procurando o campo de login pelo xpath
time.sleep(8)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password,  Keys.ENTER) # Procurando o campo de senha pelo xpath
time.sleep(180)

driver.get("https://www.instagram.com/explore/tags/funnyvideos/") # Muda para a página de hashtags (no caso, #funnyvideos)

print("Dormindo 3s")
time.sleep(3)
for i in range(1, 20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Dá 20 scrolls para baixo
    print(i)
    time.sleep(4)

posts = driver.find_elements_by_tag_name('a') # Pega todos os elementos 'a' (No qual a gente está buscando somente as publicações)

post = [elem.get_attribute('href') for elem in posts] # Separa todos os elementos com 'href'


href = [href for href in post if '/p/' in href] # Verifica se todos os links  tem /p/ ()
print(href)
print(str(len(posts)))


for i in href: # Laço para abrir todos os links
    driver.get(i) # Abrir link
    driver.execute_script("window.scrollTo(0, document.body.srollHeight);") # Dá um scroll até o final da página
    try: # Tenta clicar no botão de like
        driver.find_element_by_class_name('wpO6b ').click() 
        time.sleep(15)
    except Exception as e: # Se não conseguir, apresenta 'not like'
        print("not like") 
        time.sleep(5)



