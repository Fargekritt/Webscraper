from bs4 import BeautifulSoup
import requests
import lxml


source = requests.get("http://coreyms.com").text

soup = BeautifulSoup(source, "lxml")

for article in soup.find_all("article"):
    headline = article.h2.a.text
    print(headline)

    # print(soup.prettify())


# def find_url():
#     pass


# def find_pic():
#     pass
