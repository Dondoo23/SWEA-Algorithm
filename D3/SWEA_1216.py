import sys
sys.stdin = open("input.txt","r")
def turn(m, arr):
    for i in range(100):
        for j in range(100-m+1):
            if arr[i][j] == arr[i][j+m-1]: # 양 끝값이 같으면 안쪽 확인
                for r in range(1, m//2):
                    if arr[i][j+r] != arr[i][j+m-1-r]:
                        break
                    if r==m//2-1 and arr[i][j]==arr[i][j+m-1]:
                        return True
        
        #for j in range(100-m+1):    
            if arr[j][i]==arr[j+m-1][i]:
                for k in range(1, m//2):
                    if arr[j+k][i]!=arr[j+m-1-k][i]:
                        break
                    if k==m//2-1 and arr[j+k][i]==arr[j+m-1-k][i]:
                        return True
    return False        
                
                
T = 10
for test_case in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(100)]
    for m in range(100, 1, -1):
        ans = turn(m,arr)
        if ans:     
            print(f'#{test_case} {m}') 
            break