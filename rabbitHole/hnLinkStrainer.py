import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

http = httplib2.Http()
response = http.request("https://news.ycombinator.com/item?id=12778836")

f = open("links.txt", "a")

for link in BeautifulSoup(response, parseOnlyThese = SoupStrainer("a")):
    if link.has_key("href"):
        f.write(str(link["href"]) + "\n")
