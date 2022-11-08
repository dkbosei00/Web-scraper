import requests
from bs4 import BeautifulSoup
from secrets import username, password
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Facebook login URL
URL = "https://www.facebook.com"

#To prevent GUI from popping up
options = Options()
options.headless = True

#Accessing the URL in Chrome
driver = webdriver.Chrome(options=options)
driver.get(URL)
time.sleep(5)

#Passing in log in credentails
email = driver.find_element(By.ID, "email")
pswrd = driver.find_element(By.ID, "pass")
email.send_keys(username)
time.sleep(1)
pswrd.send_keys(password)
time.sleep(3)

#Submitting log in form
email.submit()
time.sleep(10)

#Switching from normal facebook to "mbasic" facebook to get better access to elements. The URL of the relevant post
driver.get("https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=2703580726352647&av=100001571227847&eav=AfZGj_f0bEpdT64asSwJHoGJlGH9o74XbgMJ7KhCNW2nTJb4ZgYLCIijIQ0WENTphEY&paipv=0&ext=1668163793&hash=AeQlCeK1ywdiO8_Ze-s&refid=13")

#Assigning page content to a variable
html = driver.page_source
driver.quit()

#Parsing HTML content of page to access the individual elements
soup = BeautifulSoup(html, "html.parser")

# This function was used to print out the HTML content from the previous line. "prettify()" makes content readable
# print(soup.prettify())

#Locating specific tag needed to get names of all who liked the post
names = soup.find_all('h3')

#Skipping every other iteration of h3's found in order to be left with just names
for name in names[::2]:
    print(name.text)

