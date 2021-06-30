""" import base64
import requests
import urllib
import binascii
from PIL import Image
import io

url ='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHcAAAB3CAMAAAAO5y+4AAAAVFBMVEX///9mZmZjY2NfX19bW1tXV1f8/Pzo6Ohvb29qamrb29vw8PD09PSkpKR6enqHh4fi4uLS0tLGxsaVlZW8vLzMzMy1tbWurq6NjY2bm5uBgYF0dHRc/6yQAAADvklEQVRoge2a2XLkIAxFDQK877v9//852J3MGNKdIKMiNTO5D/3SLk6xSEhCUfSjv00qHqe+V4Gp+VSnICAJy81nLjhjjO8huWpgwE7xKiA2XwRj4blNCuw3tw6Gbc+NfRPMobAZv2CZGANhGwPLeBwGm6cmdguDjWq4YhlMYbCTYKbyINjYwsIaBBstYE03zKlqpUkVgYy3Ns5ysDuh4dZ0myDYaDZ3Vw5hsMpcZlGGwWpXZZjQEggbZVfjhTpYnDFeuBAwnBv+BBmh3LLB5aIOZEDvXK4lZJ2FpGovmez7tnZFWKqWUtZhUsUhqhOmmnFe+6Xuy655OabOUcp+S1Ktql6nzHcVVFvuHACOrdS/+zo+udnzsazY+c15zo7vk7X1QBdDxeHqDfWQ6dIZ6GLsEwDrijg+rIa7K94lwh7vtBuNfpuMyspUPvnm8V3V3qHm9asR9ZCwDHGRTZW0Iw7jM7niF7vlnw15oFPxbDkMwY6NfAb5xZBu4hznVWYa7HHAMOAPcbEHGJG6dHRYTLiXsa/OC0quoYjaabFp58YtPzUgNLZ3zJkyys1l4BzdVpSrDI5rrMM1Kss9JNw9dEI4Xele7bBzPB9hUoiebrq8cr+Ac8JVFgjPPBA65t4dGy1085WIq9fM8byEKmVldC7S3WNEtNuLKWXRWRGuEL2RcVEltILu5hWY7Y3prAgwMbtdb/QQx+TilFc+JmAn5KIK7//AfL9tnb/pXKHsiJArMNVZQvsFzK1P6K94guAWhEEs5mApwlwB9UJJGF4xhuBSpoKYp1HKRJ/v7lzCuA5lwoRx7CHn0M56m/EU4o2Ftsbg/mBImnUjgnfKfPAEOxoT7QYz97rKRLrBWsItgI9pN5gddTOn/JuyrvIQF6uDIc/UC60F7GuDIow5LmCHyg5pve5N0mGLSYvPDzlVlBT9fN1uJloffUg6PefE1FzXStaH9hdPScfQ0m4I8ZR7JasnnbB0TpVIJ4xpMaQ80pgHM6ttzguLamQZyCacol5EFVXlDtsLRnQtYWr9D9E8iaJeYR+iWOk7HXeFP/ded1TrvdI3u2V9vQfilc6U38Ukbndl5T6xFqqSZCm+7y/BqyW5eQ0+24VeY9EOwwLzZ2NzIWBby3JJQT6Fw+bbCZUn9uHiUvTdu4WobKrlh0Ye6bG371LrZVgOMllbu89sXFNxWRfgNC2rWXU0dWmmgGp+3kpWtGui/z7bw8RC1V+osnlL0mrt4k8OS9EM5bJt9Uza1aiK3OWk2K1+P/o/9QuuazK9pg4CqQAAAABJRU5ErkJggg=='


response = urllib.request.urlopen(url)
test = response.file.read()
imageStream = io.BytesIO(test)
imageFile = Image.open(imageStream)
print(type(imageFile)) """



""" from requests_html import HTMLSession
from bs4 import BeautifulSoup

import time
import urllib

from binascii import a2b_base64

from selenium import webdriver
import numpy as np
import cv2

from selenium.webdriver.common.keys import Keys



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--headless")  

chrome_driver = "C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe" 
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

def getPrices(tk):
    driver.get("https://www.tradingview.com/") 


    dropdown1 = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/form/div/button')
    dropdown1.click()
    dropdown = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/form/div/div/span[2]')
    dropdown.click()


    searchinput = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/form/label/tv-autocomplete[2]/input')
    searchinput.send_keys(tk)
    searchinput.send_keys(Keys.RETURN)


    companyName = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[2]/div[1]/h1/div/div')
    price = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[1]').text
    percentChange = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/span[1]').text
    priceChange = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/span[2]').text
    print(companyName.get_attribute('innerHTML'))
    print(price)
    print(percentChange)
    print(priceChange)



def getLogo(tk):
        driver.get(f"https://www.google.com/search?q={tk}+stock")

        images = driver.find_elements_by_tag_name('img')
        for image in images:
            if image.get_property('width') == 119:
                test = (image.get_attribute('src'))


        response = urllib.request.urlopen(test)
        with open('image.jpg', 'wb') as f:
            f.write(response.file.read())



getPrices('aal') """


from os import write
import requests_html
from requests_html import HTMLSession
import re

session = HTMLSession()
""" 
r = session.get('https://finance.yahoo.com/quote/fnmas')

# r.html.render()

companyName = r.html.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1', first=True)
currentPrice = r.html.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]', first=True)
change = r.html.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[2]', first=True).text.split()
priceChange = change[0]
percentChange = change[1]

print(companyName.text)
print(currentPrice.text)
print(priceChange)
print(percentChange)

session.close """


""" with open('text.txt', 'w') as f:
    f.write(r.text) """

r = session.get('https://www.google.com/search?q=aapl+stock')

r.html.render()


images = []



teststring = (r.text) #.encode(encoding='UTF-8',errors='strict')




cutString = str(teststring.split("FZylgf", 1)[1])
# cutstring2 = cutString.split("LuVEUc B03h3d", 1)[0]


regex = re.findall("(data:image+/(?:jpeg|png)+;base64,.*?)';", str(cutString))

workinglink = (regex[0].split("\\")[0]) 
 
equalCountLink = workinglink.replace('data:image/png;base64,','').replace('data:image/jpeg;base64,','')

print(equalCountLink)
lengthlink = (len(equalCountLink))

if lengthlink % 4 == 0:
    print (workinglink)
elif lengthlink % 4 == 1:         
    print (f'{equalCountLink}===')
elif lengthlink % 4 == 2:         
    print (f'{equalCountLink}==')
else:      
    print (f'{workinglink}=')