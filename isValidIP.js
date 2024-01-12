/*
identify valid IPv4 addresses in dot-decimal format. 
IPs should be considered valid if they consist of four octets, 
with values between 0 and 255, inclusive.
*/

function isValidIP(str) {
    if (typeof str !== 'string'){ return false}
    else if (str === ''){ return false}
    else {
        let arr = str.split('.')
        if (arr.length !== 4) { return false}
        for (let i = 0;i < arr.length;i++) {
            if (arr[i] === '') { return false}
            else if (0 <= arr[i] <= 255) { return false}
            else if (arr[i].match(/[^0-9]/g)) { return false}
        }
    }
    
    return true
}

console.log('01. 02.03'.split('.'))
