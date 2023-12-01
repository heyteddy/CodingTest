def solution(n, m, x, y, queries):
    answer = 0
    top, bottom, right, left = x, x, y, y
    # 공이 도착하는 지점에서 queries를 거꾸로 돌려 가능한 시작점의 범위
    queries.reverse()
    
    for direction, dx in queries:
        if direction == 0: # 열 감소, <-
            if right+dx < m: # 오른쪽으로 이동거리가 열보다 작으면
                temp = (right+dx)
            else:
                temp = m-1 # 
                
            if left == 0:
                right = temp
            else:
                left = left+dx
                right = temp
        
        if direction == 1: # 열 증가 ->
            if left-dx >= 0:
                temp = (left-dx)
            else:
                temp = 0
                
            if right == m-1:
                left = temp
            else:
                left = temp
                right = right-dx
        
        if direction == 2: # 행 감소
            if bottom+dx < n:
                temp = bottom+dx
            else:
                temp = n-1
            if top == 0:
                bottom = temp
            else:
                top = top+dx
                bottom = temp
        
        if direction == 3: # 행 증가
            if top-dx >= 0:
                temp = top-dx
            else:
                temp = 0
                
            if bottom == n-1:
                top = temp
            else:
                top = temp
                bottom = bottom-dx
                
        if left > m-1 or right < 0 or top > n-1 or bottom < 0:
            break
        else:
            answer = ((bottom-top) + 1) * ((right-left)+1)
    return answer