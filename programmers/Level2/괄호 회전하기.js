function isRight(s, numberObj) {
    const stack = []
    for (let i = 0; i < s.length; i++) {
        if (stack.length) {
            if (numberObj[s[i]] > 0) {
                stack.push(s[i])
            } else {
                let closeParen = stack.pop()
                if (numberObj[closeParen] + numberObj[s[i]] !== 0) {
                    return false
                }
            }    
        } else {
            if (numberObj[s[i]] > 0) {
                stack.push(s[i])
            } else {
                return false
            }
        }
    }
    
    if (stack.length) {
        return false
    } else {
        return true
    }
}


function solution(s) {
    let arr = s.split('')
    let answer = 0
    const numberObj = {
        '(': 1,
        ')': -1,
        '[': 2,
        ']': -2,
        '{': 3,
        '}': -3
    }
    
    for (let j = 0; j < arr.length; j++) {
        if (isRight(arr, numberObj)) {
            answer++
        }
        arr.push(arr.shift())
    }
    
    return answer
}

let s = "[](){}"
console.log(solution(s))