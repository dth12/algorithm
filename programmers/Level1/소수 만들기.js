function solution(nums) {
  let answer = 0;
  const count = Array.from({length:3000}, () => 1)
  const limit = parseInt(Math.sqrt(3000)) + 1
  for (let i=2; i < limit; i++) {
      for (let j=2*i; j < 3000; j+=i) {
          count[j] = 0
      }
  }
  for (let i=0; i < nums.length; i++) {
      for (let j=i+1; j < nums.length; j++) {
          for (let k=j+1; k < nums.length; k++) {
              var number = nums[i] + nums[j] + nums[k]
              if (count[number] === 1) {
                  answer += 1
              }
          }
      } 
  }
  return answer
}