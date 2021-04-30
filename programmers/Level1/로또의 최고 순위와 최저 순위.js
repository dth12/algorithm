function solution(lottos, win_nums) {
    let answer = []
    let exactNum = 0
    let possibleNum = 0
    
    const zeros = lottos.filter((lotto) => {
        return lotto === 0
    })
    
    const exact = lottos.filter((lotto) => {
        return win_nums.some((win_num) => {
            return lotto === win_num
        })
    })
    
    possibleNum = zeros.length
    exactNum = exact.length
    
    answer = [7-(exactNum+possibleNum), 7-exactNum]
    if ( answer[0] >= 6 ) {
        answer[0] = 6
    }
    if ( answer[1] >= 6 ) {
        answer[1] = 6
    }
    
    return answer;
}