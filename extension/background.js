console.log('background script loaded')
function processRequest(response) {
    console.log(response.url)
}

chrome.webRequest.onCompleted.addListener(processRequest, {
    urls: ['https://streetviewpixels-pa.googleapis.com/*'],
    types: ['image'],
})
