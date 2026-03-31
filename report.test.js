const { sortPages } = require("./report.js")
const {test,expect} = require('@jest/globals')

//normalizeURL takes a URL input and returns a normalized URL string. 
//ex: it should remove the protocol (http:// or https://) and any trailing slashes from the URL. It should also convert the URL to lowercase.

test('sortPages 2 pages', () => {

    //'https://wagslane.dev/path' : 1,
    //'https://wagslane.dev/' : 3
    const input = {
        'https://example.com/path': 1,
        'https://example.com/': 3
    }

    const actual = sortPages(input)
    const expected = [
        ['https://example.com/', 3],
        ['https://example.com/path', 1]
    ]

    expect(actual).toEqual(expected)
})

test('sortPages 5 pages', () => {

    //'https://wagslane.dev/path' : 1,
    //'https://wagslane.dev/' : 3
    const input = {
        'https://example.com/path': 1,
        'https://example.com/': 3, 
        'https://example.com/path2': 5, 
        'https://example.com/path3': 6, 
        'https://example.com/path4': 9, 
        'https://example.com/path5': 10, 
    }

    const actual = sortPages(input)
    const expected = [
        ['https://example.com/path5', 10],
        ['https://example.com/path4', 9],
        ['https://example.com/path3', 6],
        ['https://example.com/path2', 5],
        ['https://example.com/', 3],
        ['https://example.com/path', 1]
    ]

    expect(actual).toEqual(expected)
})