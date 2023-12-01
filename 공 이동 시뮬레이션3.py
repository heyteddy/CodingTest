# https://prgms.tistory.com/108 참조
def solution(n, m, x, y, queries):
    # 목표지점 변수 생성
    top, left, bottom, right = x, y, x, y
    
    # 쿼리를 역순으로 돌아서 정답 칸에서 시작
    for direction, dx in reversed(queries):
        if direction == 0: # 열 감소 <-
            if left == 0: # 시작 col이 0인 경우
                right = min(m-1, right+dx) # 끝 cols의 범위를 갱신(끝 열값과 오른쪽으로 이동한 값 중 작은것 선택)
            else:
                if left+dx >= m: return 0 # 시작 col을 우측으로 dx만큼 이동한 결과가 m보다 크거나 같으면 return 0
                left = min(m-1, left+dx) # 시작, 끝 갱신
                right = min(m-1, right+dx)
                
        elif direction == 1: # 열 증가 ->
            if right == m-1: # 끝 열이 m-1인 경우(입력받은 값이 m으로 m-1)
                left = max(0, left-dx) # left 범위 갱신
            else: # 끝 열이 m-1이 아닌경우
                if right-dx < 0:
                    return 0
                left = max(0, left-dx) # left, right 갱신
                right = max(0, right-dx)
                
        elif direction == 2: # 행 감소
            if top == 0: # 행 시작이 0인 경우
                bottom = min(n-1, bottom+dx) # 끝 행 갱신
            else: # 행 시작이 0이 아닌 경우
                if top+dx >= n: # 시작 행을 밑으로 dx만큼 이동한 결과가 n보다 크면 return 0
                    return 0
                top = min(n-1, top+dx) # 시작, 끝 갱신
                bottom = min(n-1, bottom+dx)
                
        else: # 행 증가
            if bottom == n-1: # 끝 행이 n-1인 경우
                top = max(0, top-dx) # 첫 행을 갱신
            else:
                if bottom+dx < 0: # 끝 행을 위로 dx만큼 이동한 결과가 0보다 작으면 return 0
                    return 0
                top = max(0, top-dx) # 시작, 끝 갱신
                bottom = max(0, bottom-dx)
                
    return (bottom-top+1)*(right-left+1) # 출발점이 될 영역의 칸 수 return하였다