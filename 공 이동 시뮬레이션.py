def solution(n, m, x, y, queries): # 도착하는 행 x, 열 y
    top, bottom, left, right = x, x, y, y
    
    # 프로그래머스 블로그 참고, 모든 격자에 공이 있다고 생각
    for direction, dx in queries[::-1]: # 방향, 거리
        if direction == 0: # 열 감소, <-
            if left != 0: # 0에 있는 공들은 그냥 둬야함. right가 증가하면서 영역 회복
                left += dx # 이동한 거리만큼 추가
                if left > m-1: # 만약 left가 열(m-1)크기보다 커지면
                    left = m-1 # left는 더이상 이동할 수 없어서 최대값
            right += dx
            if right > m-1:
                right = m-1
        
        elif direction == 1: # 열 증가, 거꾸로 생각하면 열 감소 ->
            left -= dx
            if left < 0:
                left = 0
            if right != m-1: # 열이 가장 큰 값이 아닌 경우
                right -= dx
                if right < 0: # 열이 0보다 작은 경우
                    right = 0
                    
        elif direction == 2: # 행 감소, 거꾸로 생각하면 행 증가
            if top != 0:
                top += dx
                if top > n-1:
                    top = n-1
            bottom += dx
            if bottom > n-1:
                bottom = n-1
        
        elif direction == 3: # 행 증가
            top -= dx
            if top < 0:
                top = 0
            if bottom != n-1:
                bottom -= dx
                if bottom < 0:
                    top = 0
        # 모든 공을 다 떨어뜨리면 끝  
        if top > n-1 or bottom < 0 or left > m-1 or right < 0:
            return 0
        
        # 시작점의 개수, 즉, 남아있는 공의 개수를 의미
        return (bottom-top+1)*(right-left+1)