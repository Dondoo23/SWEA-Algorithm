import sys
sys.stdin = open("input.txt","r")

def bfs(s,e):
    q = []
    v = [0]*(V+1)
    q.append(s)
    v[s]=1

    while q:
        c = q.pop(0)
        if c==e:
            return v[e]-1
        for n in adj[c]:
            if v[n]==0:
                q.append(n)
                v[n]=v[c]+1
    return 0

T = int(input())

for test_case in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)
    S,G = map(int,input().split())

    ans = bfs(S,G)