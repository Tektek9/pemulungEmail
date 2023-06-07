import re
from selenium import webdriver
print("/     \ |=== /===>")
print("|  |  | |=== \===\\")
print(" \/ \/  |=== <===/")
print("Web Email Scrapper")
print("Created by KuliOnline11")
a = input(str("Silahkan masukan url:"))
chrome_driver = '/chromedriver_win32'
driver = webdriver.Chrome(chrome_driver)
driver.get(a)

page_source = driver.page_source

PemulungEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

kumpilanEmail = []
for madakno in re.finditer(PemulungEmail, page_source):
    kumpilanEmail.append(madakno.group())

for i, email in enumerate(kumpilanEmail):
    print(email)