import sys
sys.stdin = open("input.txt","r")

T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split()) # N * N 의 파리지도 M * M 의 파리채
    graph = []
    for i in range(N): # 파리 지도 입력
        lst = list(map(int,input().split()))
        graph.append(lst)

    K = N-M+1 # 필터(파리채)를 map(파리지도)에 씌웠을때 인덱스 K까지만 가면 된다
    ans = []
    sum = 0

    for i in range(K):
        for j in range(K):
            for r in range(M): # i,j 는 필터를 씌웠을때의 가장 좌측 상단 인덱스
                for u in range(M): # 거기부터 파리채의 크기만큼 모든 파리의 수 더해주기
                    sum += graph[i+r][j+u]
            ans.append(sum) # 더한 값을 ans 배열에 입력
            sum = 0
            

    result = max(ans) # 더한 값들이 모두 입력되어 있는 배열에서 최댓값 찾기
    print(f'#{test_case} {result}')