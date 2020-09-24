import random
import time
 
def checkSort(a,n):
    isSorted = True
    for i in range(1,n):
        if a[i] > a[i+1]:
            isSorted = False
        if (not isSorted):
            break
    if (isSorted):
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

def selectionSort(a,n):
    for i in range (1,n):
        minIndex = i
        for j in range(i+1, n+1):
            if a[minIndex] > a[j] :
                minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]


N = 5000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
selectionSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 선택 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))


N = 10000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
selectionSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 선택 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))


N = 15000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
selectionSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 선택 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

print()

N = 5000
b = []
b.append(-1)
for i in range(N):
    b.append(i)
start_time = time.time()
selectionSort(b,N)
end_time = time.time() - start_time
print('정렬된 값이 삽입된 배열의 선택 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 10000
b = []
b.append(-1)
for i in range(N):
    b.append(i)
start_time = time.time()
selectionSort(b,N)
end_time = time.time() - start_time
print('정렬된 값이 삽입된 배열의 선택 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 15000
b = []
b.append(-1)
for i in range(N):
    b.append(i)
start_time = time.time()
selectionSort(b,N)
end_time = time.time() - start_time
print('정렬된 값이 삽입된 배열의 선택 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

print()

N = 5000
b = []
b.append(-1)
for i in range(N,0,-1):
    b.append(i)
start_time = time.time()
selectionSort(b,N)
end_time = time.time() - start_time
print('역순으로 값이 삽입된 배열의 선택 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 10000
b = []
b.append(-1)
for i in range(N,0,-1):
    b.append(i)
start_time = time.time()
selectionSort(b,N)
end_time = time.time() - start_time
print('역순으로 값이 삽입된 배열의 선택 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 15000
b = []
b.append(-1)
for i in range(N,0,-1):
    b.append(i)
start_time = time.time()
selectionSort(b,N)
end_time = time.time() - start_time
print('역순으로 값이 삽입된 배열의 선택 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))