import sys

n=int(input())

if n==4 or n==7:
    print(-1)
    sys.exit()

if n==6:
    print(2)
    sys.exit()

def sugar(a):
    
    if a%5==0 :
        
        print(a//5)

    elif a%5==1 or a%5==3 :

        print((a//5)+1)

    elif a%5==2 or a%5==4 :

        print((a//5)+2)

sugar(n)