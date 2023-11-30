
T = int(input())

for test_case in range(1,T+1):
    v = [0] * 5001 # 노선 정보를 담기 위한 리스트
    arr = []
    N = int(input()) # 노선의 개수
    for i in range(N):
        a, b = map(int,input().split())
        for j in range(a,b+1): # a와 b 사이의 모든 노선을 1씩 증가
            v[j] += 1

    P = int(input())
    for i in range(1,P+1):
        c = int(input()) # 출력하고자 하는 정류장
        arr.append(v[c]) # 해당 정류장의 노선 개수 입력

    print(f'#{test_case}', *arr)