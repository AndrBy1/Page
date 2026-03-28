const { JSDOM } = require('jsdom') //JSDOM is a library that allows us to parse HTML and manipulate the DOM in Node.js. We use it to extract URLs from the HTML body.

function getURLsFromHTML(htmlBody, baseURL){
    const urls = []
    const dom = new JSDOM(htmlBody)
    //we use "a" because we want to get the href attribute of the "a" tag
    const linkElements = dom.window.document.querySelectorAll('a')
    for(const linkElement of linkElements){
        //urls.push(linkElement.href)
        console.log(linkElement.href)

    }
    return urls
}

function normalizeURL(urlString) {
    const urlObj = new URL(urlString) //URL constructor alreadys lowercases hostname and pathname

    const hostPath = `${urlObj.hostname}${urlObj.pathname}`

    if (hostPath.length > 0 && hostPath.slice(-1) === '/') {
        return hostPath.slice(0, -1)
    }
    return hostPath
}

module.exports = {
    normalizeURL,
    getURLsFromHTML
}