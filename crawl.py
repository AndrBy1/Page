#from bs4 import BeautifulSoup # This is a third-party library that we will use to parse HTML. We will install it using pip.
#import tldextract
#from html.parser import HTMLParser
from MyHTMLParser import MyHTMLParser
from urllib.parse import urlparse

def getURLsFromHTML(htmlBody, baseURL):
    urls = []
    dom = MyHTMLParser(htmlBody)
    linkElements = dom.findQuery("a")
    print("Link Elements: " + str(linkElements))
    for linkElement in linkElements:
        #print("Link Element: " + linkElement[:-1])
        try:
            urlObj = urlparse(baseURL + linkElement).geturl()
            print("URL Object: " + str(urlObj))
        except Exception as e:
            print("Error parsing URL: " + str(e))
            continue
        if linkElement.startswith("/"):
            
            #relative URL
            urls.append(urlObj)
        else:
            #absolute URL
            urls.append(linkElement)
    #print("Link Elements: " + str(linkElements))
    print("URLs: " + str(urls))
    return urls

def normalizeURL(url):
    urlObj = urlparse(url)
    #print("URL Object: " + str(urlObj))
    
    # .hostname naturally lowercases the hostname
    hostname = urlObj.hostname

    # strip the subdomain from the hostname
    subdomains = ["www.", "m.", "mobile.", "blog.", "news.", "shop.", "store.", "app.", "web.", "dev.", "test.", "staging."]
    for subdomain in subdomains:
        if hostname.startswith(subdomain):
            hostname = hostname[len(subdomain):]
            break

    # combine the hostname and path
    hostPath = hostname + urlObj.path
    print("Host: " + hostname)

    if len(hostPath) > 0 and hostPath.endswith('/'):
        hostPath = hostPath[:-1]


    return hostPath