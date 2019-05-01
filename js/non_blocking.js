const nothing = () => {}

console.log('start sleeping')
setTimeout(nothing, 3000)   // ms 단위          non-block callback stack     비동기 방식
console.log('end of program')


// python blocking.py 처럼 동작하게 하려면...
const logEnd = () => {
    console.log('end of program')
}
console.log('start sleeping') 
setTimeout(logEnd, 3000)



function first() {
    console.log('first')
}

function second() {
    console.log('second')
}

function third() {
    console.log('third')
}

first()
setTimeout(second, 0)       //0초라고 해도 다녀와~
third()

// func1() 를 호출 했을 때
// 아래와 같이 콘솔에 출력
// func1
// func3
// func2


function func1() {
    console.log('func1')
    func2()
}

function func2() {
    setTimeout(() => console.log('func2'), 0)
    func3()
}

function func3() {
    console.log('func3')
}

func1()
