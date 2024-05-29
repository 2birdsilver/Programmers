def solution(arr):
    num=1
    max_value = max(arr)
    
    while True:
        temp = max_value * num
        count = 0
        for i in arr:
            if temp % i != 0:
                break
            count += 1
            if count == len(arr):
                return temp
        num += 1