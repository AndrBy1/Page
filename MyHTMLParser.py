
class MyHTMLParser:
    htmlLinks = []
    def __init__(self, htmlStr):

        self.htmlStr = htmlStr

    def findQuery(self, query):
        for line in self.htmlStr.splitlines():
            if ("<" + query) in line:
                print("Found query: " + query)
                print("Line: " + line)
                if 'href="' in line:
                    print("Found href: " + line.split('href="')[1].split('"')[0])
                    self.htmlLinks.append(line.split('href="')[1].split('"')[0] + " ")
                    #return line.split('href="')[1].split('"')[0]
        return self.htmlLinks
            

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag: " + tag)
    