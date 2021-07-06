// n회 t분 간격, 최대 m명
// 모든 버스를 못타게 됐을 때: 마지막 버스, 마지막 사람보다 1분 먼저.
// 마지막 버스가 비어있을 때: 마지막 버스 도착 시간에 탐.
// 마지막 버스는 꽉 차있지만, 나머지 버스는 탈 수 있을 때, 마지막부터 보면서 가장 처음으로 탈 수 있는 
function numToTime(num) {
    let hour = String(Math.floor(num / 60))
    let minute = String(num % 60)
    
    if (hour.length === 1) hour = '0' + String(hour)
    if (minute.length === 1) minute = '0' + String(minute)
    
    return hour + ':' + minute
}


function solution(n, t, m, timetable) {
    // busInfo 버스 탄 사람을 기록함. [<버스 시간>, <탄 사람의 수>, <마지막으로 탄 사람의 시간>]
    let waitTable = Array(1440).fill(0)
    let busRecords = Array(0)
    let answer = 0
    
    for(let time of timetable) {
        let [hour, minute] = time.split(':')
        let idx = Number(hour) * 60 + Number(minute)
        waitTable[idx]++
    }
    
    for(let i = 0; i < n; i++) {
        let busTime = 540 + i * t
        let passenger = 0
        let busRecord = [busTime, passenger, 0]
        for (let j = 1; j <= busTime; j++) {
            if (passenger === m) break
            if (waitTable[j]) {
                if (waitTable[j] + passenger <= m) {
                    passenger += waitTable[j]
                    waitTable[j] = 0
                } else {
                    let num = m - passenger
                    passenger += num
                    waitTable[j] -= num
                }
                busRecord[2] = j
            }
        }
        busRecord[1] = passenger
        busRecords.push(busRecord)
    }
    
    busRecords.reverse()
    for (let[busTime, total, last] of busRecords) {
        if (total < m) {
            answer = busTime
            break
        }
        
        if (total === m) {
            answer = last - 1
            break
        }
    }
     
    return numToTime(answer)
}