import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(input())
    map = []
    for i in range(8):
        map.append(list(input()))

    # 가로로 쭉 가면서 회문 찾기
    result = 0
    for i in range(8):
        for r in range(8):
            first = r
            # 현재 위치에서 찾으려는 회문의 길이만큼 더한 인덱스
            last = r+n-1
            count = 0
            if last < 8:
                # 앞 뒤에서 같이 하나씩 오면서 찾을거기 때문에 절반만
                for j in range(n//2):
                    if map[i][first] == map[i][last]:
                        first += 1
                        last -= 1
                        count += 1
                    else:
                        break
                # 카운트가 n/2만큼 올라갔다는건 n/2번째까지 둘이 똑같다는 것
                if count == n//2:
                    result += 1
                    
    # 세로롤 쭉 돌면서 똑같이
    result2 = 0
    for i in range(8):
        for r in range(8):
            first = r
            last = r+n-1
            count = 0
            if last < 8:
                for j in range(n//2):
                    if map[first][i] == map[last][i]:
                        first += 1
                        last -= 1
                        count += 1
                    else:
                        break
                if count == n//2:
                    result2 += 1
    final = result + result2
    print(f'#{test_case} {final}')