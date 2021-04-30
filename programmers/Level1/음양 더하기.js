function solution(absolutes, signs) {
  let answer = 0;
  const L = absolutes.length
  
  for (let i=0; i < L; i++) {
     if (signs[i] === true) {
         answer += absolutes[i]
     } else {
         answer -= absolutes[i]
     }
  }
  
  return answer;
}