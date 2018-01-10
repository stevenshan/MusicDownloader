#https://www.google.com/search?q=(Whatever your search)
import urllib.request
import requests
from bs4 import BeautifulSoup

'''
This works but google is ass at displaying stuff so the songs are not in order. I am going to use the spotify api
artist = input("Artist: ")
album = input("Album: ")
artist = artist.replace(' ','%20')
album= album.replace(' ','%20')

url = ("https://www.google.com/search?q="+artist+"%20"+album+"%20songs")
#header is needed so that google thinks this is coming from a person not a machine
#will error without declaring a header
req =  urllib.request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    }
)

pageFile = urllib.request.urlopen(req)
pageHtml = pageFile.read()
scraper = BeautifulSoup(pageHtml,'html.parser')

for y in scraper.find_all('span',class_="st"):
    print(y.findAll("em"))'''
