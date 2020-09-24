import random, time, sys

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

# cocktailshakeSort가 너무 길어서 csSort로 줄여서 작성

def csSort(a,n):
    i, j = N, 1
    while(i>j):
        if (i+j != N): # 배열의 앞에서 뒤로 진행
            for k in range(j,i,1):
                if (a[k] > a[k+1]):
                    a[k], a[k+1] = a[k+1], a[k]
            i -= 1
        else : # 배열의 뒤에서 앞으로 진행
            for k in range(i,j,-1): 
                if (a[k-1] > a[k]):
                    a[k-1], a[k] = a[k], a[k-1]
            j += 1

N = 5000
b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
csSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 칵테일쉐이커 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

b = []
b.append(-1)
for i in range(N):
    b.append(i)
start_time = time.time()
csSort(b,N)
end_time = time.time() - start_time
print('정렬된 값이 삽입된 배열의 칵테일쉐이커 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))


b = []
b.append(-1)
for i in range(N-1,-1,-1):
    b.append(i)
start_time = time.time()
csSort(b,N)
end_time = time.time() - start_time
print('역순으로 정렬된 배열의 칵테일쉐이커 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
print()

N = 10000

b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
csSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 칵테일쉐이커 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

b = []
b.append(-1)
for i in range(N):
    b.append(i)
start_time = time.time()
csSort(b,N)
end_time = time.time() - start_time
print('정렬된 값이 삽입된 배열의 칵테일쉐이커 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))


b = []
b.append(-1)
for i in range(N-1,-1,-1):
    b.append(i)
start_time = time.time()
csSort(b,N)
end_time = time.time() - start_time
print('역순으로 정렬된 배열의 칵테일쉐이커 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

N = 15000

b = []
b.append(-1)
for i in range(N):
    b.append(random.randint(1,N))
start_time = time.time()
csSort(b,N)
end_time = time.time() - start_time
print('임의로 값이 삽입된 배열의 칵테일쉐이커 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

b = []
b.append(-1)
for i in range(N):
    b.append(i)
start_time = time.time()
csSort(b,N)
end_time = time.time() - start_time
print('정렬된 값이 삽입된 배열의 칵테일쉐이커 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))


b = []
b.append(-1)
for i in range(N-1,-1,-1):
    b.append(i)
start_time = time.time()
csSort(b,N)
end_time = time.time() - start_time
print('역순으로 정렬된 배열의 칵테일쉐이커 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))