import sys

sys.setrecursionlimit(10**8)

input=sys.stdin.readline

def alpha(dt,ac,go):
    
    dt += ac
    
    if x+dt == y and ac == 1:
        num.append(go)
    
    elif x+dt < y:
    
        if ac == 1:
            alpha(dt, ac, go+1)
            alpha(dt, ac+1, go+1)
    
        else:
            alpha(dt, ac-1, go+1)
            alpha(dt, ac, go+1)
            alpha(dt, ac+1, go+1)

T = int(input())

for i in range(T):

    x,y = map(int, input().split())
    num = []
    alpha(0,1,1)
    print(min(num))

##원본코드가 훨씬 낫다...