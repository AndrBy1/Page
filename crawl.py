#from bs4 import BeautifulSoup # This is a third-party library that we will use to parse HTML. We will install it using pip.

from MyHTMLParser import MyHTMLParser
from html.parser import HTMLParser
from urllib.parse import urlparse



def getURLsFromHTML(htmlBody, baseURL):
    urls = []
    dom = MyHTMLParser(htmlBody)
    linkElements = dom.findQuery("a")
    for linkElement in linkElements:
        print("Link Element: " + linkElement[:-1])
        urls.append(linkElement[:-1])
    #print("Link Elements: " + str(linkElements))
    return urls

def normalizeURL(url):
    urlObj = urlparse(url)
    #print("URL Object: " + str(urlObj))
    hostPath = urlObj.hostname + urlObj.path
    print("Host: " + urlObj.hostname)

    if len(hostPath) > 0 and hostPath.endswith('/'):
        hostPath = hostPath[:-1]


    return hostPath