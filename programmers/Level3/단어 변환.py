from collections import deque

def bfs(graph, begin, target, words):
    visited = {word:0 for word in words}
    queue = deque([])
    queue.append(begin)
    dist = -1
    while queue:
        dist += 1
        L = len(queue)
        # queue의 길이만큼만 반복합니다 => 거리 저장을 위해서
        for _ in range(L):
            v = queue.popleft()
            visited[v] = 1
            if v == target: return dist
            for word in graph[v]:
                if visited[word] == 0:
                    visited[word] = 1
                    queue.append(word)

    return 0
    
def solution(begin, target, words):
    # 인접 딕셔너리를 생성합니다.
    graph = dict()

    if target not in words:
        return 0
    
    # 시작 지점도 words에 포함시킵니다.
    words.append(begin)

    L = len(begin)
    # words 안에 있는 단어들로 각 자리가 하나씩 다를 때에만 인접한 단어로 저장합니다.
    for word_key in words:
        for word_value in words:
            idx = 0
            cnt = 0
            while cnt <= 1 and idx < L:
                if word_key[idx] != word_value[idx]:
                    cnt += 1
                idx += 1
            if cnt == 1:
                if word_key in graph:
                    graph[word_key].append(word_value)
                else:
                    graph[word_key] = [word_value]
    
    # 최단 거리를 bfs를 통해 찾습니다.
    answer = bfs(graph, begin, target, words)
    return answer