import random, time, sys
sys.setrecursionlimit(3002)

def quickSort(a, l, r):
    if r > l:
        v, i, j = a[r], l-1, r
        while True :
            i += 1
            while a[i] < v :
                i+=1
            j -= 1
            while a[j] > v :
                j -= 1        
            if i >= j:
                break  
            a[i], a[j] = a[j], a[i]
        a[i], a[r] = a[r], a[i]
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)

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
quickSort(a,1,N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 퀵 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 2000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1,N))
start_time = time.time()
quickSort(a,1,N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 퀵 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 3000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1,N))
start_time = time.time()
quickSort(a,1,N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 퀵 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 1000
a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
quickSort(a,1,N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 퀵 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 2000
a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
quickSort(a,1,N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 퀵 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 3000
a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
quickSort(a,1,N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 퀵 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 1000
a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
quickSort(a,1,N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 퀵 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 2000
a = []
a.append(-1)
for i in range(N,0,-1):
    a.append(i)
start_time = time.time()
quickSort(a,1,N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 퀵 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 3000
a = []
a.append(-1)
for i in range(N,0,-1):
    a.append(i)
start_time = time.time()
quickSort(a,1,N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 퀵 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)