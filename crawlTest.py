import crawl

def test_getURLsFromHTML_Absolute():
    #parser = crawl.MyHTMLParser()
    print("testing getURLsFromHTML absolute")
    inputHTML = '''
    <html>
        <body>
            <a href="https://blog.boot.dev/path/"> 
                Boot.dev Blog
            </a>
        </body>
    </html>
    '''

    inputBaseURL = "https://blog.boot.dev/path/"
    actual = crawl.getURLsFromHTML(inputHTML, inputBaseURL)
    expected = ["https://blog.boot.dev/path/"]
    print("Actual: " + str(actual))
    print("Expected: " + str(expected))
    assert actual == expected

def test_getURLsFromHTML_Relative():
    print("testing getURLsFromHTML relative")
    inputHTML = '''
    <html>
        <body>
            <a href="/path/"> 
                Boot.dev Blog
            </a>
        </body>
    </html>
    '''

    inputBaseURL = "https://blog.boot.dev"
    actual = crawl.getURLsFromHTML(inputHTML, inputBaseURL)
    expected = ["https://blog.boot.dev/path/"]
    print("Actual: " + str(actual))
    print("Expected: " + str(expected))
    assert actual == expected

def test_getURLsFromHTML_Both():
    print("testing getURLsFromHTML both")
    inputHTML = '''
    <html>
        <body>
            <a href="https://blog.boot.dev/path1/">
                Boot.dev Blog Path One
            </a>
            <a href="/path2/"> 
                Boot.dev Blog Path Two
            </a>
        </body>
    </html>
    '''

    inputBaseURL = "https://blog.boot.dev"
    actual = crawl.getURLsFromHTML(inputHTML, inputBaseURL)
    expected = ["https://blog.boot.dev/path1/", "https://blog.boot.dev/path2/"]
    print("Actual: " + str(actual))
    print("Expected: " + str(expected))
    assert actual == expected

def test_getURLsFromHTML_invalid():
    print("testing getURLsFromHTML invalid")
    inputHTML = '''
    <html>
        <body>
            <a href="invalid"> 
                Invalid URL
            </a>
        </body>
    </html>
    '''

    inputBaseURL = "https://blog.boot.dev"
    actual = crawl.getURLsFromHTML(inputHTML, inputBaseURL)
    expected = []
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
    test_getURLsFromHTML_Absolute()
    test_getURLsFromHTML_Relative()
    test_getURLsFromHTML_Both()
    test_getURLsFromHTML_invalid()