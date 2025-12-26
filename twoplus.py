#numbers = [5, 0, 2, 7, 1]
numbers = list(map(int, input("정수 입력: ").split()))

#2) 두 숫자 합치기
n_1 = [] #숫자 합친 배열

for i in range(len(numbers) - 1) :
    for n in range(len(numbers) - i - 1) : 
        add = numbers[i] + numbers[i+n+1]
        if add not in n_1 :
            n_1.append(add)

#3) numbers 조건에 따라 0 이상 100 이하로
n_2 = []
for i in range(len(n_1)) :
    if n_1[i] >=2 and n_1[i] <= 100 :
        n_2.append(n_1[i])

print (n_2)

#4) 오름차순으로 정렬하기
for j in range(len(n_2) - 1) :
    for i in range(len(n_2) - 1) :
        if n_2[i] > n_2[i+1] :
            k = n_2[i]
            n_2[i] = n_2[i+1]
            n_2[i+1] = k

print (n_2)
