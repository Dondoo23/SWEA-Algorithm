def result(t, count):
    global ans
    ans *= n
    count += 1
    if count == m:
        return
    result(t+1, count)
    
        
T = 1
for test_case in range(1,T+1):
    tc = int(input())
    n, m = map(int,input().split()) # n의 m제곱
    t = 1
    ans = 1
    count = 0
    result(t, count)
    print(ans)