import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
  arr = input()
  mem = list() # 입력받은 0011등의 문자열을 숫자 0 0 1 1 로 만들기 위해서
  for number in arr:
    mem.append(int(number))
  result = [0] * len(mem)
  
  count = 0
  for i in range(len(mem)):
    if result[i]!=mem[i]:  # 같지 않다면
      if result[i]==0: #  같지 않고 0이라면
        for j in range(i, len(mem)): # 해당 위치부터 마지막까지 모두 1로
          result[j] = 1
      else: # 같지 않고 1이라면
        for r in range(i, len(mem)): # 해당 위치부터 마지막까지 모두 0으로
          result[r] = 0
      count += 1
  print(f'#{test_case} {count}')