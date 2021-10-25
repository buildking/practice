import sys

def alpha(plused,plus,count):
    
    plused += plus
    if x+plused == y and plus == 1:
        num.append(count)
    elif x+plused < y:
        if plus == 1:
            alpha(plused,plus,count+1)
            alpha(plused,plus+1,count+1)
        else:
            alpha(plused,plus-1,count+1)
            alpha(plused,plus,count+1)
            alpha(plused,plus+1,count+1)

T = int(input())

for i in range(T):
    x,y = map(int, sys.stdin.readline().split())
    num = []
    alpha(0,1,1)
    print(min(num))