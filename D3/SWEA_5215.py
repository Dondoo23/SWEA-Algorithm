# import sys
# sys.stdin = open("sample_input.txt","r")

def dfs(n,start,score,kcal): # start는 중복을 방지하기 위해서
    global max_score
    if n==N: # n개 모두 체크했으면 return
        return

    if score > max_score:
        max_score = score

    for i in range(start, N):
        if kcal+arr[i][1] <= L:
            dfs(n+1,i+1,score+arr[i][0],kcal+arr[i][1]) # start+1을 해서 중복방지

T = int(input())

for test_case in range(1,T+1):
    N, L = map(int,input().split())

    arr = []
    for _ in range(N):
        t, k = map(int,input().split())
        arr.append([t,k])

    max_score = 0
    dfs(0,0,0,0)
    print(f'#{test_case} {max_score}')