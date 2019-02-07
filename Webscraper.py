from bs4 import BeautifulSoup
import requests
import lxml


source = requests.get("http://coreyms.com").text

soup = BeautifulSoup(source, "lxml")

print(soup.prettify())


def find_url():
    pass


def find_pic():
    pass
