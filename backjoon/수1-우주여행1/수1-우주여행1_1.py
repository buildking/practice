import sys

input = sys.stdin.readline

testnum = int(input())

for test in range(testnum):

    c, d = map(int, input().split())

    r = d- c

    if r<4 :

        print(r)

        continue

    i=0

    while r > 0 :
        
        i += 1
        r -= 2*i
        
        if r <= 0:
        
            print(2 * i)
            break

        elif r <= i+1:
        
            print(i*2+1)
            break