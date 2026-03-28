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
test('getURLsFromHTML', () => {
    const inputHTMLBody = `
<html>
    <body>
        <a href="https://blog.boot.dev"> 
            Boot.dev Blog
        </a>
    </body>
</html>
`
    const inputBaseURL = "https://blog.boot.dev"
    const actual = getURLsFromHTML(inputHTMLBody, inputBaseURL)
    const expected = ["https://blog.boot.dev/"]
    expect(actual).toEqual(expected)

})