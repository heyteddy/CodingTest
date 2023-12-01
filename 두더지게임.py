# 8x8 크기의 판을 생성하고 0으로 초기화
board = [[0] * 8 for _ in range(8)]

# 두더지의 위치 정보를 입력받음
for i in range(8):
    row = input().strip()  # 공백을 제거하여 문자열로 입력 받음
    for j in range(8):
        board[i][j] = int(row[j])  # 문자열을 정수로 변환하여 판에 반영

# 두더지가 올라올 수 있는 칸의 개수를 세는 변수 초기화
count = 0

# 판을 순회하면서 두더지가 올라올 수 있는 칸인지 확인
for i in range(8):
    for j in range(8):
        if board[i][j] == 0:
            count += 1

# 결과 출력
print(count)