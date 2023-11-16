#import sys
# sys.stdin = open("input.txt","r")

T = int(input())

for test_case in range(1,T+1):
    H, W = map(int, input().split()) # 높이가 H, 너비가 W
    graph = []

    flag = []
    for i in range(H):
        a = list(input())
        graph.append(a)

        if '<' in a: # 탱크의 위치와 방향 정보 저장
            index = a.index('<')
            flag.append(i)
            flag.append(index)
            flag.append(1) # 방향
        if 'v' in a:
            index = a.index('v')
            flag.append(i)
            flag.append(index)
            flag.append(2)
        if '>' in a:
            index = a.index('>')
            flag.append(i)
            flag.append(index)
            flag.append(3)
        if '^' in a:
            index = a.index('^')
            flag.append(i)
            flag.append(index)
            flag.append(4)

    N = int(input()) # 사용자가 넣을 입력의 개수
    arr = list(input())

    for item in arr:
        if item=='U':
            flag[2] = 4 # 일단 탱크의 방향을 바꿔준다(이동은 아래 조건문에서)
            if flag[0]-1 >= 0 and graph[flag[0]-1][flag[1]]=='.':
                graph[flag[0]][flag[1]] = '.'
                graph[flag[0]-1][flag[1]] = '^'
                flag[0] -= 1
            else:
                graph[flag[0]][flag[1]] = '^'

        if item=='D':
            flag[2] = 2
            if flag[0]+1 < H and graph[flag[0]+1][flag[1]]=='.':
                graph[flag[0]][flag[1]] = '.'
                graph[flag[0]+1][flag[1]] = 'v'
                flag[0] += 1
            else:
                graph[flag[0]][flag[1]] = 'v'

        if item=='L':
            flag[2] = 1
            if flag[1]-1 >= 0 and graph[flag[0]][flag[1]-1]=='.':
                graph[flag[0]][flag[1]] = '.'
                graph[flag[0]][flag[1]-1] = '<'
                flag[1] -= 1
            else:
                graph[flag[0]][flag[1]] = '<'

        if item=='R':
            flag[2] = 3
            if flag[1]+1 < W and graph[flag[0]][flag[1]+1]=='.':
                graph[flag[0]][flag[1]] = '.'
                graph[flag[0]][flag[1]+1] = '>'
                flag[1] += 1
            else:
                graph[flag[0]][flag[1]] = '>'

        if item=='S':
            if flag[2]==1:
                for i in range(flag[1],-1,-1):
                    if graph[flag[0]][i]=='#': # 강철벽이 있다면 거기서 그냥 break
                        break
                    if graph[flag[0]][i]=='*': # 강철벽 없이 쭉 가서 그냥 벽 만나면 파괴
                        graph[flag[0]][i]='.'
                        break
            if flag[2]==2:
                for i in range(flag[0],H):
                    if graph[i][flag[1]] == '#':
                        break
                    if graph[i][flag[1]]=='*':
                        graph[i][flag[1]]='.'
                        break
            if flag[2]==3:
                for i in range(flag[1],W):
                    if graph[flag[0]][i] == '#':
                        break
                    if graph[flag[0]][i]=='*':
                        graph[flag[0]][i] = '.'
                        break
            if flag[2]==4:
                for i in range(flag[0],-1,-1):
                    if graph[i][flag[1]] == '#':
                        break
                    if graph[i][flag[1]]=='*':
                        graph[i][flag[1]] = '.'
                        break

    print(f'#{test_case}',end=' ')
    for i in range(H):
        for j in range(W):
            print(graph[i][j],end='')
        print()
