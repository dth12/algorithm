let ans = 0

function dfs(row, N, cnt, visited, visited_c, visited_c_re) {
    if (row === N) {
        if (cnt === N) {
            ans++   
        }
        return 0
    }
    
    for (let c = 0; c < N; c++) {
        let colIdx = row + c
        let colReIdx = row - c + N - 1
        if (visited[c] === 0 && visited_c[colIdx] === 0 && visited_c_re[colReIdx] === 0) {
            visited[c] = 1
            visited_c[colIdx] = 1
            visited_c_re[colReIdx] = 1
            dfs(row + 1, N, cnt + 1, visited, visited_c, visited_c_re)
            visited[c] = 0
            visited_c[colIdx] = 0
            visited_c_re[colReIdx] = 0
        }
    }   
}

function solution(n) {
    const visited = new Array(n).fill(0)
    const visited_c = new Array(n * 2 - 1).fill(0)
    const visited_c_re = new Array(n * 2 - 1).fill(0)
    
    dfs(0, n, 0, visited, visited_c, visited_c_re)
    return ans
}

console.log(solution(8))