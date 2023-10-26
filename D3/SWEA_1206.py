T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1,11):
    n = int(input()) # 건물의 개수 입력
    height = list(map(int,input().split())) # 건물의 높이 리스트로 입력
    result = 0
    for i in range(2,n-2): # 가장 왼쪽2, 가장 오른쪽2는 무조건 0이므로 제외하고 루프
        if height[i] > height[i-2] and height[i] > height[i-1] and height[i] > height[i+1] and height[i] > height[i+2]: # 2칸 전, 1칸 전, 1칸 후, 2칸 후 건물의 높이보다 현재 건물이 높다면
            result += height[i] - max(height[i-2], height[i-1], height[i+1], height[i+2]) # 그 중 가장 높은 건물의 층을 현재 건물의 층에서 빼준다.
    print('#{num} {res}'.format(num=test_case, res=result))
