var url = 'https://www.geoguessr.com/api/v3/games/hP36pyYhiOCRFqB7'
var obj = {
    token: 'hP36pyYhiOCRFqB7',
    lat: 14.292564247357502,
    lng: 15.59274358740232,
    timedOut: false,
}

fetch(url, {
    method: 'POST',
    body: JSON.stringify(obj),
    headers: {
        cookie: '_ncfa=sbPcHGmPWIikR3%2BghToENpADg0ZPIBZvTv24gBRo7ng%3DkRqDsSlNUcnDFw6aSfimgTXCJlCfBHehw9lixat6GYCDK0xDB1ooEfm%2B3KXKcT%2Fw; devicetoken=4755E63736; StatsSend=true',
        'Content-Type': 'application/json',
    },
})
    .then((response) => response.text())
    .then((html) => console.log(html))
