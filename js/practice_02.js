let getMin = (a,b) => {
    
    if (a > b) {
        return b
    }
    return a
}

let conCat = (str1, str2) => {
    return `${str1} - ${str2}`
}

let checkLongStr = (string) => {
    if (string.length > 10) {
        return true
    }
    return false 
}

if (checkLongStr(conCat('Happy', 'Hacking'))) {
    console.log('LONG STRING')
} else {
    console.log('SHORT STRING')
}
