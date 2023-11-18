import sys
#sys.stdin = open("input.txt","r")

def dfs(c,v):
    global ans
    ans = max(ans,len(v)) # 최대값 갱신

    for n in adjL[c]: # c와 연결된 노드 하나씩
        if n not in v: # 방문하지 않은 노드인 경우
            dfs(n,v+[n])


T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())

    adjL = [[] for _ in range(N+1)] # 인접 행렬
    for _ in range(M):
        s, e = map(int,input().split())
        adjL[s].append(e) # s노드에 e노드가 연결됨
        adjL[e].append(s) # 그 반대도 연결됨

    ans = 0
    for s in range(1,N+1):
        dfs(s,[s])
    print(f'#{test_case} {ans}')