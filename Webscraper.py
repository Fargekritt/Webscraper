from bs4 import BeautifulSoup
import requests
import lxml
import re


source = requests.get("http://coreyms.com").text
soup = BeautifulSoup(source, "lxml")


for links in soup.find_all("h2"):
    print(links)

# pattern = re.compile("Linux")
# matches = pattern.finditer(source)
# for match in matches:
#     print(match)
