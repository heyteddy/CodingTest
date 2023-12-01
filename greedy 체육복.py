def solution(n, lost, reserve):
    r_lost = set(lost) - set(reserve) # 순수하게 도난사람 번호 리스트
    r_reserve = set(reserve) - set(lost) # 순수하게 여벌 체육복 사람 번호 리스트
    for i in r_lost:
        if i+1 in r_reserve: # 본인 번호보다 1 큰 학생이 여벌있는 경우
            r_reserve.remove(i+1) # 여벌 리스트에서 제거
        elif i-1 in r_reserve:
            r_reserve.remove(i-1)
        else: # 앞 뒤로 여벌 체육복을 가지고 있는 학생이 없는 경우, 수업을 들을 수 없다.
            n -= 1 # 
    return n

print(solution(5, [2,4], [1,3,5]))