import sys
sys.stdin = open("input.txt", "r")

T = 10 # 10
for test_case in range(1,T+1):
    N = int(input()) # 원본 암호문의 길이
    ori = list(map(int,input().split())) # 원본 암호문 입력
    n_insert = int(input()) # 입력할 명령의 횟수
    insert = list(input().split()) # 명령어 입력

    

    for i in range(n_insert): # 명령의 횟수만큼(명령 횟수만큼 자르고 리스트 다시 생성할 것)
        ind = int(insert[1]) # 0번째는 I, 1에는 새로운 암호입력할 인덱스, 2에는 새로운 암호들의 개수, 3부터 암호들
        n = int(insert[2])
        
        ori_first = ori[:ind] # 입력할 인덱스 기준으로 분할
        ori_second = ori[ind:]
        
        ori_insert = insert[3:3+n] # 입력할 암호들
        ori = ori_first + ori_insert + ori_second # 분할한 원본 암호문 사이에 새로운 암호들 끼워넣고 다시 합치기
        insert = insert[3+n:] # 새로운 암호들이 모두 나오고 다시 I가 나오는 부분부터 새롭게 리스트 시작
    result = []
    for item in ori: # 명령어 입력할때 문자로 받았으므로 암호들도 문자로 생성돼있는 상태. 모두 정수로 바꿔줌
        result.append(int(item))
        
    print(f'#{test_case}', end=' ')
    for i in range(10):
        print(result[i], end=' ')
    print()
