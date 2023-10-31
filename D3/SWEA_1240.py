import sys
sys.stdin = open("input.txt", "r")

password = ['1011000','1001100','1100100','1011110','1100010','1000110','1111010','1101110','1110110','1101000']

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int,input().split())

    output = -1
    for i in range(n):
        line = input()
        if int(line) != 0 and output == -1:
            line = str(int(line[::-1])) # 문장을 역순으로 바꿔서 뒤에 있는 0들을 삭제
        
            data = []
            for j in range(8):
                data.insert(0, password.index(line[j*7:j*7+7])) # insert(0,x)은 x를 맨 앞에 넣으므로 다시 역순으로 입력(원래 순서대로 비밀번호 저장)
            if ((data[0] + data[2] + data[4] + data[6]) * 3 + data[1] + data[3] + data[5] + data[7]) % 10 == 0:
                output = sum(data)
            else:
                output = 0
    print(f'#{test_case} {output}')

