function solution(n, works) {
    
    const total = works.reduce((acc, cur) => {
        return acc + cur
    })
    
    if ( total <= n ) {
        return 0
    }
    
    let cnt = 0
    works.sort((a, b) => {
        return b - a
    })
    
    while ( cnt < n ) {
        works[0] -= 1
        let idx = 0
        while ( idx < works.length - 1 ) {
            if ( works[idx] < works[idx + 1]) {
                [ works[idx], works[idx + 1] ] = [ works[idx + 1], works[idx] ]
            } else {
                break
            }
            idx++
        }
        cnt++
    }
    
    const answer = works.reduce((acc, cur) => {
        return acc + cur ** 2
    }, 0)
    
    return answer
    
}