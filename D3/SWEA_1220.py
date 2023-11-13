import sys
sys.stdin = open("input.txt","r")

T = 10
for test_case in range(1, T+1):
    size = int(input())
    arr = [list(map(int,input().split())) for _ in range(size)] # map 입력
    total_res = 0 # 결과값
    
    for i in range(size):
        flag = 0
        for j in range(size):
            if arr[j][i] == 1:
                flag = 1 
            elif arr[j][i] == 2:
                if flag: # flag가 1을 만나 활성화돼있는 상태라면 교착
                    total_res += 1
                    flag = 0
    print(f'#{test_case} {total_res}')