#import sys
#sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T+1):
    # 평탄화 시도 횟수
    count = int(input())
    # 높이 입력
    height = list(map(int, input().split()))

    max_i = height.index(max(height))
    min_i = height.index(min(height))

    for i in range(count):
        # 가장 높은 높이와 가장 낮은 높이의 차이가 1보다 크면 반복(일단 count만큼만 반복)
        if max(height) - min(height) > 1:
            height[height.index(max(height))] -= 1
            height[height.index(min(height))] += 1
        # 1이 되면 평탄화 완료이므로 바로 break
        else:
            break
    # 높이 차이 출력
    result = max(height)-min(height)
    print('#{i} {r}'.format(i=test_case, r=result))