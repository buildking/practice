#####프로토타입#####

# import sys

# input=sys.stdin.readlines

# #테스트케이스 개수
# cycle=int(input())

# #사람
# pp=[][]

# #0층 인구 기입
# for pu in range(14):
    
#     pp[0][pu]=pu+1

# #테스트케이스만큼 루프
# for i in range(cycle):

#     #층
#     f=int(input())

#     #호
#     w=int(input())

#     #1층부터 차례차례 기입. 몇층일지 모르기 때문에 매번 다시.
#     for tmpf in range(1,f):

#         #층 합산 초기화
#         wsum=0
        
#         #새로 시작하는 층 첫 호실 선언
#         wsum += pp[tmpf-1][0]

#         #첫 호실에 입력
#         pp[tmpf][0] = wsum

#         for tmpw in range(1, w):

#             for prw in range(1, tmpw):

#                 wsum += pp[tmpf-1][prw-1]

#             pp[tmpf][tmpw] = wsum + pp[tmpf-1][tmpw]

#     print(pp[f][w])



        





