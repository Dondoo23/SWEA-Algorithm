import sys
sys.stdin = open("test_input.txt","r")

T = 10 # 10
for test_case in range(1, T+1):
    num = int(input())
    find_str = input() # 찾을 문자열
    search_str = input() # 얘로부터 위 문자열을 찾을 것
    ans = search_str.find(find_str) # ans 에 첫번째 찾은 문자열의 인덱스(못찾았다면 -1)
    
    count = 0
    while (ans != -1): # 찾았다면
        count += 1
        search_str = search_str[ans+len(find_str):] # 찾은 인덱스부터 찾으려던 문자열의 길이를 더하고 그 위치부터 새롭게 문자열 생성
        ans = search_str.find(find_str) # 새롭게 생성한 문자열로부터 다시 찾음
    print(f'#{test_case} {count}')