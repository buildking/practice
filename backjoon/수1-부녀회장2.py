#2차원배열로 풀기
cycle=int(input())

#호실 2차원배열
pp=[[1 for col in range(25)] for row in range(25)]

for r in range(1, 20):
    for c in range(1, 20):
        pp[r][c]=pp[r-1][c]+pp[r][c-1]

for j in range(cycle):

    x=int(input())

    y=int(input())

    print(pp[x+1][y-1])
