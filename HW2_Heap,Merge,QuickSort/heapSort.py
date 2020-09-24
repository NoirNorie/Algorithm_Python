import random, time

def heapify(a,h,m):
    v = a[h]
    j = 2*h
    while(j <= m):
        if (j < m and a[j] < a[j+1]):
            j += 1
        if (v >= a[j]):
            break
        else:
            a[int(j/2)] = a[j]
        j *= 2
    a[int(j/2)] = v

def heapSort(a, n):
    for i in range(int(n/2), 0, -1):
        heapify(a,i,n)
    for i in range(n-1, 0, -1):
        a[1], a[i+1] = a[i+1], a[1]
        heapify(a,1,i)

def checkSort(a,n):
    isSorted = True
    for i in range(1,n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 완료")

N = 1000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1,N))
start_time = time.time()
heapSort(a,N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 히프 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 2000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1,N))
start_time = time.time()
heapSort(a,N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 히프 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 3000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1,N))
start_time = time.time()
heapSort(a,N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 히프 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 1000
a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
heapSort(a,N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 히프 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 2000
a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
heapSort(a,N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 히프 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 3000
a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
heapSort(a,N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 히프 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 1000
a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
heapSort(a,N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 히프 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 2000
a = []
a.append(-1)
for i in range(N,0,-1):
    a.append(i)
start_time = time.time()
heapSort(a,N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 히프 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 3000
a = []
a.append(-1)
for i in range(N,0,-1):
    a.append(i)
start_time = time.time()
heapSort(a,N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 히프 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)