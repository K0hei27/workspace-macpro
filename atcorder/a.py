N=int(input())
l = list(map(int,input().split()))
f = 0
flag=True
while flag:
    for i in range(N-1):
        if l[i] % 2 == 0:
            l[i] /= 2
        else:
            flag=False
            print(f)
            break
    f += 1
