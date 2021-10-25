import sys

input = sys.stdin.readline

testnum = int(input())

for test in range(testnum):

    c, d = map(int, input().split())

    r = d- c

    if r<4 :

        print(r)

        continue

    dm=0

    while True :

        dm+=1

        if dm**2>=r:

            xp=dm**2

            np=(dm-1)**2

            rp = np + ((xp-np)/2)

            if r > rp :

                print((2*dm)-1)

            elif r==np+1:

                print(2*(dm-1))

            else :

                print(2*(dm-1)-1)

            break