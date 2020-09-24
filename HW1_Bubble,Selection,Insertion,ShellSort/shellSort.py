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

def shellSort(a,n):
    h = 1
    while h < n :
        h = 3*h+1
    while h > 0:
        for i in range(h+1,n+1):
            v = a[i]
            j = i
            while j > h and a[j-h] > v:
                a[j] = a[j-h]
                j = j-h
            a[j] = v
        h = int(h/3)

N = 5000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))


N = 10000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))


N = 15000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 20000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 25000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 30000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 35000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 40000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 45000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 50000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 55000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 60000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 65000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 70000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 75000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 80000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 85000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 90000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 95000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 100000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 150000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 200000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 250000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 300000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 350000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 400000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 450000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 500000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 550000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 600000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
shellSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 쉘 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))