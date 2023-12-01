input() # 한 줄 입력(문자열)
input().split() # 공백으로 구분된 문자열 입력
int() # 정수값으로 변환
float() # 실수값으로 변환
map() # 여러 요소를 하나의 함수에 매핑

# hello 입력
st = input()

# 45 입력
N = int(input())

# 1 2 3 입력
n1, n2, n3 = map(int,input().split())

# 3.14 입력
F = float(input())

# 1.2, 2.3, 3.4 입력
f1, f2, f3 = map(float,input().split())

# one two three 리스트로 입력
arr = input().split()

# 1 2 45 43 리스트로 입력
arr = list(map(int,input().split()))

# 한 줄에 있는 공백없는 한자리 숫자들을 각각 숫자로 리스트에 저장 1234
arr = list(map(int,input()))

# N*N 공백없는 한자리 숫자들을 2차원 arr에 저장
n = int(input())
arr = [list(map(int,input())) for _ in range(n)]

# N*N 공백있는 한자리 숫자들을 2차원 arr에 저장
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

# 0값 10개를 가진 1차원 리스트 생성
arr = [0] * 10

# 0값 3 * 3 개를 가진 2차원 리스트 생성
arr = [[0] * 3 for _ in range(3)]

# 2차원 arr을 저장 후 사방을 0으로 감싸기
n = int(input())
start = [[0] * (n+2)]
end = [[0] * (n+2)]
arr = [[0] + list(map(int,input().split())) + [0] for _ in range(n)]
res = start + arr + end

for i in range(len(res)):
    print(*res[i])