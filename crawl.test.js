const { normalizeURL, getURLsFromHTML } = require("./crawl.js")
const {test,expect} = require('@jest/globals')

//normalizeURL takes a URL input and returns a normalized URL string. 
//ex: it should remove the protocol (http:// or https://) and any trailing slashes from the URL. It should also convert the URL to lowercase.

test('normalizeURL strip protocol', () => {
    const input = 'https://example.com/path'
    const actual = normalizeURL(input)
    const expected = 'example.com/path'
    
    expect(actual).toEqual(expected)

})

test('normalizeURL strip trailing slash', () => {
    const input = 'https://example.com/path/'
    const actual = normalizeURL(input)
    const expected = 'example.com/path'

    expect(actual).toEqual(expected)

})

test('normalizeURL strip capitals', () => {
    const input = 'https://EXAMPLE.COM/path/'
    const actual = normalizeURL(input)
    const expected = 'example.com/path'

    expect(actual).toEqual(expected)

})

test('normalizeURL strip http', () => {
    const input = 'http://example.com/path/'
    const actual = normalizeURL(input)
    const expected = 'example.com/path'

    expect(actual).toEqual(expected)

})

//getURLsFromHTML takes an HTML body and a baseURL as input and returns an array of all the URLs found in the HTML body. 
//ex: if the HTML body contains <a href="http://example.com/path/">Link</a>, then the function should return ['example.com/path'].
test('getURLsFromHTML absolute', () => {
    const inputHTMLBody = `
<html>
    <body>
        <a href="https://example.com"> 
            example.com 
        </a>
    </body>
</html>
`
    const inputBaseURL = "https://example.com"
    const actual = getURLsFromHTML(inputHTMLBody, inputBaseURL)
    const expected = ["https://example.com/"]
    expect(actual).toEqual(expected)

})

test('getURLsFromHTML relative', () => {
    const inputHTMLBody = `
<html>
    <body>
        <a href="/path/"> 
            example.com 
        </a>
    </body>
</html>
`
    const inputBaseURL = "https://example.com"
    const actual = getURLsFromHTML(inputHTMLBody, inputBaseURL)
    const expected = ["https://example.com/path/"]
    expect(actual).toEqual(expected)

})

test('getURLsFromHTML both', () => {
    const inputHTMLBody = `
<html>
    <body>
        <a href="https://example.com/path1/"> 
            example.com Path One
        </a>
        <a href="/path2/"> 
            example.com Path Two
        </a>
    </body>
</html>
`
    const inputBaseURL = "https://example.com"
    const actual = getURLsFromHTML(inputHTMLBody, inputBaseURL)
    const expected = ["https://example.com/path1/", "https://example.com/path2/"]
    expect(actual).toEqual(expected)

})


test('getURLsFromHTML Invalid', () => {
    const inputHTMLBody = `
<html>
    <body>
        <a href="invalid"> 
            Invalid URL
        </a>
    </body>
</html>
`
    const inputBaseURL = "https://example.com"
    const actual = getURLsFromHTML(inputHTMLBody, inputBaseURL)
    const expected = []
    expect(actual).toEqual(expected)

})