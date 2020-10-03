import random, time

def naturalMergeSort(a,N):
    ## 분할 단계
    b,c =[], []
    c.append(a[1])
    for i in range(2,N+1):
        if (a[i-1] < a[i]): ## 작은수 -> 큰수의 형태인 경우
            c.append(a[i])
        else:               ## 큰수 -> 작은수의 형태인 경우
            b.append(c)
            c = []
            c.append(a[i])
    b.append(c) ## 남은 부분배열 처리

    ## 합병 단계
    if (len(b[0]) == N):     ## run이 하나만 존재한다면 이미 정렬된 경우이므로 바로 반환
        return b[0]          ## 오름차순으로 이미 정렬된 배열이 들어온 경우일 것임

    result = merge(b[0],b[1])
    p = 2
    while(len(result) != N): ## 분할한 배열들을 다 사용할 때 까지
        result = merge(result,b[p])
        p += 1
        
    return result

## 합병 정렬
def merge(L,R):
    result = []
    x, y = 0,0

    while(x < len(L) and y < len(R)):
        if (L[x] >= R[y]):
            result.append(R[y])
            y += 1
        else:
            result.append(L[x])
            x += 1

    if (x != len(L)):
        for i in range(x,len(L)):
            result.append(L[i])
    if (y != len(R)):
        for i in range(y,len(R)):
            result.append(R[i])

    return result

N = 1000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1,N))
start_time = time.time()
b = []
b = naturalMergeSort(a,N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))

a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
b = []
b = naturalMergeSort(a,N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))

a = []
a.append(-1)
for i in range(N-1,-1,-1):
    a.append(i)
start_time = time.time()
b = []
b = naturalMergeSort(a,N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))

N = 2000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1,N))
start_time = time.time()
b = []
b = naturalMergeSort(a,N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))

a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
b = []
b = naturalMergeSort(a,N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))

a = []
a.append(-1)
for i in range(N-1,-1,-1):
    a.append(i)
start_time = time.time()
b = []
b = naturalMergeSort(a,N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))

N = 3000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1,N))
start_time = time.time()
b = []
b = naturalMergeSort(a,N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))

a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
b = []
b = naturalMergeSort(a,N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))

a = []
a.append(-1)
for i in range(N-1,-1,-1):
    a.append(i)
start_time = time.time()
b = []
b = naturalMergeSort(a,N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f'%(N,end_time))