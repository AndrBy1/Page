const { normalize, normalizeURL } = require("./crawl.js")
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