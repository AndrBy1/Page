import crawl

def test_getURLsFromHTML():
    #parser = crawl.MyHTMLParser()
    inputHTML = '''
    <html>
        <body>
            <a href="https://blog.boot.dev"> 
                Boot.dev Blog
            </a>
        </body>
    </html>
    '''

    inputBaseURL = "https://blog.boot.dev"
    actual = crawl.getURLsFromHTML(inputHTML, inputBaseURL)
    expected = ["https://blog.boot.dev"]
    print("Actual: " + str(actual))
    print("Expected: " + str(expected))
    assert actual == expected


def test_normalizeURL():
    print("Testing normalizeURL strip protocol")
    assert crawl.normalizeURL("https://www.example.com/path/") == "example.com/path"

    print("Testing normalizeURL strip trailing slashes")
    assert crawl.normalizeURL("https://www.example.com/path/") == "example.com/path"
    
    print("Testing normalizeURL strip capitals")
    assert crawl.normalizeURL("https://EXAMPLE.COM/path/") == "example.com/path"

    
if __name__ == "__main__":
    
    test_normalizeURL()
    test_getURLsFromHTML()