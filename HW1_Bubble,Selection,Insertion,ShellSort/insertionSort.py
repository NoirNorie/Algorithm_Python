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

def insertionSort(a,n):
    for i in range(2,n+1):
        v = a[i]
        j = i
        while a[j-1] > v:
            a[j] = a[j-1]
            j = j-1
        a[j] = v

N = 5000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
insertionSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 삽입 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))


N = 10000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
insertionSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 삽입 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))


N = 15000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
insertionSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 삽입 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

print()

N = 5000
b = []
b.append(-1)
for i in range(N):
    b.append(i)
start_time = time.time()
insertionSort(b,N)
end_time = time.time() - start_time
print('정렬된 값이 삽입된 배열의 삽입 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 10000
b = []
b.append(-1)
for i in range(N):
    b.append(i)
start_time = time.time()
insertionSort(b,N)
end_time = time.time() - start_time
print('정렬된 값이 삽입된 배열의 삽입 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 15000
b = []
b.append(-1)
for i in range(N):
    b.append(i)
start_time = time.time()
insertionSort(b,N)
end_time = time.time() - start_time
print('정렬된 값이 삽입된 배열의 삽입 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

print()

N = 5000
b = []
b.append(-1)
for i in range(N,0,-1):
    b.append(i)
start_time = time.time()
insertionSort(b,N)
end_time = time.time() - start_time
print('역순으로 값이 삽입된 배열의 삽입 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 10000
b = []
b.append(-1)
for i in range(N,0,-1):
    b.append(i)
start_time = time.time()
insertionSort(b,N)
end_time = time.time() - start_time
print('역순으로 값이 삽입된 배열의 삽입 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 15000
b = []
b.append(-1)
for i in range(N,0,-1):
    b.append(i)
start_time = time.time()
insertionSort(b,N)
end_time = time.time() - start_time
print('역순으로 값이 삽입된 배열의 삽입 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))