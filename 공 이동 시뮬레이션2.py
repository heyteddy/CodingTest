def solution(n, m, x, y, queries):
    answer = 0
    t, l, r, b = x, y, y, x
    queries.reverse()
    
    for i, j in queries:
        if i == 0:
            temp = (r + j) if r + j < m else m - 1
            
            if l == 0: 
                r = temp
            else: 
                l, r = l + j, temp
        if i == 1:
            temp = (l - j) if l - j >= 0 else 0
            
            if r == m - 1: 
                l = temp
            else: 
                l, r = temp, r - j
        if i == 2:
            temp = (b + j) if b + j < n else n - 1
            
            if t == 0:
                b = temp
            else:
                t, b = t + j, temp
        if i == 3:
            temp = (t - j) if t - j >= 0 else 0
            
            if b == n - 1:
                t = temp
            else:
                t, b = temp, b - j
    
        if l > m - 1 or r < 0 or t > n - 1 or b < 0:
            break
    
    else:
        answer = ((b - t) + 1) * ((r - l) + 1) 
        
    return answer

