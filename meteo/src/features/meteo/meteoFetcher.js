const API_URL = "http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=xml"


export function getMeteoInfo() {
    return fetch(API_URL)
        .then(response => response.text())
}