var _ = require("lodash");
let list = ['짜장면', '짬뽕', '볶음밥',]
let numbers = _.range(1, 46)
let lottery = _.sampleSize(numbers, 6)
let pick = _.sample(list)
let menu = {
    짜장면 : 'https://previews.123rf.com/images/nontoxicguy/nontoxicguy1611/nontoxicguy161100439/66442742-%EC%9E%90%EC%9E%A5%EB%A9%B4-%EC%A7%9C%EC%9E%A5%EB%A9%B4-%EA%B2%80%EC%9D%80-%EC%BD%A9-%EC%86%8C%EC%8A%A4-%EA%B5%AD%EC%88%98.jpg',
    짬뽕: 'http://food.chosun.com/site/data/img_dir/2012/08/08/2012080802054_0.jpg',
    볶음밥: 'https://www.tefal.co.kr/medias/?context=bWFzdGVyfHJvb3R8MzMwMjB8aW1hZ2UvanBlZ3xoMmIvaGRkLzkzMzg2MjY2MDUwODYuanBnfDVjMmFmZjMyMjIxZjBlMTM0MjZlNTk2MGRiMGMyZjgzZmM4MGZkYWNmYWVmNGFmZmVkNjU5NTQ3Y2I4Y2FiYzc',
}

console.log(`오늘의 메뉴는 ${pick} 입니다. `)
console.log(menu[pick])
console.log(`행운의 번호: ${lottery}`)

// let getMin = (a,b) => {
    
//     if (a > b) {
//         return b
//     }
//     return a
// }

// let getMin = (a, b) => {
//     let min;
//     if (a>b) {
//         min = b
//     } else {
//         min = a
//     }
//     return min
// }


let getMinFromArray = nums => {
    let min = Infinity // 양의 무한대 

    // nums 배경을 돌면서 min 변수와 비교하여 최소 값을 찾는다.
    for (num of nums) {
        if (min > num) {
            min = num
        }
    }
    return min
}

ssafy = [1, 2, 3, 4, 5,]
console.log(getMinFromArray(ssafy))

const myObject = {
    key : 'Value'
}

console.log(myObject['key'])

