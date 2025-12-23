numbers = [5,0,2,7,2]


def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot = arr[n//2]
    left_ary, mid_ary, right_ary = [], [], []
    for number in arr:
        if number<pivot:
            left_ary.append(number)
        elif number>pivot:
            right_ary.append(number)
        else:
            mid_ary.append(number)    
    return quick_sort(left_ary)+mid_ary+quick_sort(right_ary)

def solution(numbers):
    n = len(numbers)
    temp = []
    for i in range(n):
        for j in range(i+1, n):
            temp.append(numbers[i]+numbers[j])

    temp = list(set(temp))    
    answer = quick_sort(temp)
    return answer
