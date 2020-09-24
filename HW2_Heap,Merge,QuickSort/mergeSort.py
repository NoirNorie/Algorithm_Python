import random, time

def mergeSort(a,l,r):
    if (r > l):
        mid = int((r+l)/2)
        mergeSort(a, l, mid)
        mergeSort(a, mid+1, r)

        for i in range(mid+1, l, -1):
            b[i-1] = a[i-1]
        i -= 1

        for j in range(mid, r):
            b[r+mid-j] = a[j+1]
        j += 1

        for k in range(l, r+1):
            if(b[i] < b[j]):
                a[k] = b[i]
                i += 1
            else:
                a[k] = b[j]
                j -= 1

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
b = a.copy()
mergeSort(a,1,N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 2000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1,N))
start_time = time.time()
b = a.copy()
mergeSort(a,1,N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 3000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1,N))
start_time = time.time()
b = a.copy()
mergeSort(a,1,N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 1000
a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
b = a.copy()
mergeSort(a,1,N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 2000
a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
b = a.copy()
mergeSort(a,1,N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 3000
a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
b = a.copy()
mergeSort(a,1,N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 1000
a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
b = a.copy()
mergeSort(a,1,N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 2000
a = []
a.append(-1)
for i in range(N,0,-1):
    a.append(i)
start_time = time.time()
b = a.copy()
mergeSort(a,1,N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)

N = 3000
a = []
a.append(-1)
for i in range(N,0,-1):
    a.append(i)
start_time = time.time()
b = a.copy()
mergeSort(a,1,N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))
checkSort(a,N)