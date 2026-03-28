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
    
    assert crawl.normalizeURL("https://www.example.com/path/") == "www.example.com/path"
    assert crawl.normalizeURL("https://www.example.com/path") == "www.example.com/path"
    assert crawl.normalizeURL("https://www.example.com/") == "www.example.com"
    assert crawl.normalizeURL("https://www.example.com") == "www.example.com"

    
if __name__ == "__main__":
    
    test_normalizeURL()
    test_getURLsFromHTML()