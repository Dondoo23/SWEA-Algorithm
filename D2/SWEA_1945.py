import sys
sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    ans = []
    arr = [2,3,5,7,11]

    for i in arr:
        count = 0
        while(N % i == 0):
            count += 1
            N /= i
        ans.append(count)
    print(f'#{test_case}',end=' ')
    print(*ans)