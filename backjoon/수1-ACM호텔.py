import sys

input=sys.stdin.readline

a=int(input())

for i in range(a):
    
    h, w, n = map(int, input().split())

    rh=n%h

    rw=n//h + 1
    
    if rh==0:

        rh=h
        rw-=1

    if rw >= 10 :
        print(rh, rw,sep='')

    else :
        print(rh, 0, rw,sep='')
