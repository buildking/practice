#문자열 자료형

#문자열 개수 세기(count)

>>> a="hobby"
>>> a.count('b')
>>> 2

#위치 알려주기1(find)       
>>> a='python is best choice'
>>> a.find('b')
>>> 10
>>> a.find('k')
>>> -1

#위치 알려주기2(index)
>>> a='life is too short'
>>> a.index('t')
>>> 8
>>> a.index('k')
traceback (most recent call last):
file "<stdin>", line 1, in <module>
valueerror: substring not found
#ㄴ없으면 에러!

#조인!
>>> a=','.join('abcd')
>>> print(a)

>>> a=','.join(['a','b','c','d'])
>>> print(a)

#커피++
c=10
m=300

while m:
    print('c go')
    c -= 1

    print(f'rest c {c} death')
    if not c:
        print('no c')
        break

#파일 생성, 입력, 닫기
f=open('new.txt','w')
for i in range(1,11):
    data=(f'{i} line. \n')
    f.write(data)
f.close()





#class 클래스 사용법
class djawnstlr:
    def __init__(self) :
        self.result=0
    
    def add(self, num):
        self.result+=num
        return self.result

cal1=djawnstlr()
cal2=djawnstlr()

print(cal1.add(3))
print(cal1.add(4))

print(cal2.add(5))
print(cal2.add(18))

#class fourcalculation 사칙연산 클래스로 만들기
class Fourcal:
    def __init__(self, first, second):
        self.first=first
        self.second=second
    def setdata(self, first, second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result

a=Fourcal()
a.setdata(4,2)
print(a.add())


#일단 실행, 오류발생시, 오류없을때, 최후에
#exception=오류의 부모, 오류 다 잡을 수 있음
try:#일단 실행
    f=open('none','r')
except FileNotFoundError as e:#error come
    print(str(e))
else:#not error
    data=f.read()
    print(data)
    f.close()
finally:#finally going
    f.close()
      

#두 수 비교하기
a, b = map(int,input().split())

if a>b :
    print(">")
elif a<b :
    print('<')
else :
    print('==')



#성적 관리. 점수->성적.
a=input()

a=int(a)

if a>=90 :
    print('A')
elif a>=80:
    print('B')
elif a>=70:
    print('C')
elif a>=60:
    print('D')
else :
    print('F')

#윤년 판독기
y=input()

y=int(y)

if y%100!=0 and y%4==0 or y%400==0 :
    print('1')
else :
    print('0')


#알람시계 자동 조정.
h , m = map(int,input().split())

m2 = m-45

if m2>0 or m2==0 :
    print(h, m2)
else :
    if h-1>0 :
        print(h-1, 60+m2)
    elif h-1 ==0 :
        print(0, 60+m2)
    else :
        print(23, 60+m2)

#99dan
s=int(input())

for i in range(1, 10):
    print(s, '*', i, '=', s*i)
    i+=1


#t개수만큼 입력받아서 덧셈하고 출력 처리
t=int(input())

for i in range(0,t):
    a, b=map(int,input().split())
    print(a+b)

#아주 빠르고 강력하게 t개수만큼 입력받아서 덧셈하고 출력 처리
#https://www.acmicpc.net/board/view/22716
import sys

t=int(sys.stdin.readline())

for i in range(t):
    a, b= map(int, sys.stdin.readline().split())
    print(a+b)

#입력받고 숫자나열
import sys

input=sys.stdin.readline

n=int(input())

for i in range(n):
    print(i+1)


#자료 입력받아 바로 덧셈 출력. f-string, map 사용 중점!!
import sys

input=sys.stdin.readline

n=int(input())

for i in range(n):
    i=int(i)+1
    a, b = map(int,input().split())
    print(f'Case #{i}:', a+b)

#위랑 비슷, 출력만 다른방식
import sys

input=sys.stdin.readline

n=int(input())

for i in range(n):
    i=int(i)+1
    a, b = map(int,input().split())
    print(f'Case #{i}:', a, '+', b, '=', a+b)

#star printing
import sys

input=sys.stdin.readline

m=int(input())

for i in range(m):
    i1=int(i)+1
    for j in range(i1):
        print('*', end='')
    print('')


#reverse star printing
import sys

input=sys.stdin.readline

m=int(input())

for i in range(m):
    i1=int(i)+1
    b=m-i1
    for j in range(b):
        print(' ', end='')
    for j1 in range(i1):
        print('*', end='')
    print('')



#https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline


#작은숫자 골라내기, 리스트사용 정말 중요!!
import sys

input=sys.stdin.readline

a, x = map(int,input().split())

list=input().split()

al=[]

for i in range(a):
    if int(list[i])<x :
        al.append(int(list[i]))

l=len(al)

for j in range(l):
    print(al[j], end=' ')


#루프도는 숫자 단계 출력
import sys

input=sys.stdin.readline

n=int(input())

nn=n

c=0

while 1==1 :
    
    a=nn//10
    b=nn%10

    s=a+b

    aa=s//10
    bb=s%10

    nn=b*10+bb

    c+=1

    if nn==n:
        print(c)
        break


#리스트 사용 + 소트 정렬 배열

import sys

input=sys.stdin.readline

n=int(input())

l=input().split()

al=[]

for i in range(n):
    al.append(int(l[i]))

c=sorted(al)


print(c[0], c[-1])

print(c)


#가장 큰 수 찾기 + 숫자 위치번호
import sys

input=sys.stdin.readline

m=0
x=0

for i in range(9):
    p=int(input())

    if m<p :
        m=p
        x=i+1

print(m)
print(x)


#나머지 같은 개수 찾기, 레인지 소괄호 기억해줘!!!!
import sys

input=sys.stdin.readline

f=[]
g=[]

n=10

for i in range(10):
    f.append(int(input()))
    g.append(int(f[i]%42))
    for j in range(i):
        if g[i]==g[j]:
            n-=1
            break

print(n)



#new avg
import sys

input=sys.stdin.readline

n=int(input())

t=[]

it=input().split()

for i in range(n):
    t.append(int(it[i]))

t.sort()

ns=0

for i in range(n):
    ns=ns+(t[i]/t[-1]*100)

print(ns/n)


#OX퀴즈 점수계산해주기

t=[]

for i in range(n):
    n1=input()
    t.append(n1)

##여기까지 입력 완료, t[n] 리스트로..

for i in range(n):

    s=1

    sn=0

    m=t[i]

    l=len(m)

    for j in range(l):

        if m[j]=='O':

            if m[j-1]=='O' and j!=0 :

                s+=1          

            sn=sn+s

        else :
            s=1
    
    print(sn)

#평균이상비율 출력해주기
import sys

input=sys.stdin.readline

n=int(input())

for i in range(n):

    u=0

    tu=[]

    s=input().split()

    st=int(s[0])

    for j in range(int(st)):
        tu.append(int(s[j+1]))

    for k in range(int(st)):
        u=u+int(tu[k])

    av=u/int(s[0])
    
    tuover = 0

    for avi in range(st):
        if int(tu[avi])>av :
            tuover += 1

    rs=tuover/st*100

    print(f'{rs:.3f}%')



#a 안의 모든 수 더하기!! 진짜 짧다..
def solve(a):
    ans=sum(a)
    return ans    




#발상이 대단한사람
a = 1
def d(a):  
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    d_array = []
    res = []
    for a in range(0,10000):
        if a<10:
            n1 = a//1
            d_array.append(a+n1)
        elif (a>=10) and (a<100):
            n1 = a//10
            n2 = a%10
            d_array.append(a+n1+n2)
        elif (a>=100) and (a<1000):
            n1 = a//100
            n2 = (a%100)//10
            n3 = a%10
            d_array.append(a+n1+n2+n3)
        elif (a>=1000)and (a<10000):
            n1 = a//1000
            n2 = (a%1000)//100
            n3 = (a%100)//10
            n4 = a%10
            d_array.append(a+n1+n2+n3+n4)
    d_array.sort()


    temp = list(range(10000))
    res = list(set(temp)-set(d_array))
    res.sort()

##이부분 유의해서 볼만함!!
    for j in range(0, len(res)):
        print(res[j])
    return res
d(a)

#한수(숫자배치가 등차) 개수 찾기 문가
def han(n):

    n1=0
    n2=0
    n3=0
    n4=0
        
    c=0
    x=0
    isum=0
        
    for i in range(n):



        x=i+1

        if 100>x :
            c+=1
            
        elif 1000>x and x>=100 :
            n1=x%10
            n2=(x%100)//10
            n3=x//100
            isum = (n1-n2) + (n3-n2)
            if isum == 0 :
                c+=1

    return(c)

sol=int(input())

print(han(sol))


#alphabet searching
a=input()

l=[]

for i in range(97, 123):

    fi=a.find(chr(i))

    l.append(fi)

print(*l)

#문자열 반복해서 출력하는법!!!! 매일 복습해야하는 이유..
import sys

input=sys.stdin.readline

a=int(input())

for i in range(0, a):

    b,c = map(str, input().split())

    b=int(b)
    c=str(c)
    
    l=len(c)
    
    for k in range(l):

        print(b*c[k], end =''if k != l-1 else '\n')


#단어 개수찾기, if문 안에 ()로 조건 넣을 수 있다!!
a=input()

b = a.count(' ')

if (a[0] == ' ' and a[-1] != ' ') or (a[0] != ' ' and a[-1] == ' ') :
    print(b)
elif a[0] == ' ' and a[-1] == ' ' :
    print(b-1)
else :
    print(b+1)


#큰 수 찾기, 공백 없이 출력하기!!!
import sys

input=sys.stdin.readline

a,b = map(int,input().split())

fa1=a%10
fb1=b%10

fa2=(a%100)//10
fb2=(b%100)//10

fa3=a//100
fb3=b//100

if fa1>fb1 :
    print(fa1,fa2,fa3, sep='')
elif fa1<fb1 :
    print(fb1,fb2,fb3, sep='')
else :
    if fa2>fb2 :
        print(fa1,fa2,fa3, sep='')
    elif fa2<fb2 :
        print(fb1,fb2,fb3, sep='')
    else :
        if fa3>fb3 :
            print(fa1,fa2,fa3, sep='')
        elif fa3<fb3 :
            print(fb1,fb2,fb3, sep='')
        else:
            print('?')


#할머니댁 전화기 암호로 걸기, 딕셔너리 써봤다!! 성공!!
st=input()

nst=len(st)

s=0

p = {2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],9:['W','X','Y','Z']}

for i in range(len(st)) :
    for j in range(2,10) :
        if st[i] in p[j] :
            s += j
            break


print(nst+s)


#크로아티아문자 단어 개수 찾기!! if문 떡칠이지만 통과!!
st=input()

nst=len(st)

for i in range(1, len(st)) :
    if st[i] == '=':
        if st[i-1] == 's':
            nst -= 1
        elif st[i-1] == 'c':
            nst -= 1
        elif st[i-1] == 'z':
            if st[i-2] == 'd' and i>1:
                nst -= 2
            else :
                nst -= 1

    elif st[i] == '-':
        if st[i-1] == 'c':
            nst -= 1
        elif st[i-1] == 'd':
            nst -= 1

    elif st[i] == 'j':
        if st[i-1] == 'l':
            nst -= 1
        elif st[i-1] == 'n':
            nst -= 1

print(nst)

#그룹단어 체커, 이제 조금 len함수 사용, list함수 사용 익숙해지는듯!!
go=int(input())

l=[]

for n in range(0,go):
    
    st=input()

    nst=len(st)

    change = 0

    l.clear()

    l.append(st[0])

    for i in range(0, len(st)-1) :
        
        if st[i] != st[i+1] :
            
            ##이쪽 포문 주목할만함!!
            for j in range(len(l)-1) :
                if st[i+1] in l :
                    change += 1
                    break

            l.append(st[i+1])

    if change != 0:
        go -= 1

print(go)

#벌집!!!!! 점화식으루다가
x=int(input())

r = 0

s = 1

while True :

    if s>=x :
        break

    r += 1

    s += 6*r

print(r+1)

#달팽이 나무오르기. 경우의수 계산해서 적용!!!
import sys

input=sys.stdin.readline

u, d, h = map(int, input().split())

if u>h:
    print('1')

elif (h-u)%(u-d) != 0:
    print((h-u)//(u-d)+2)

elif (h-u)%(u-d) == 0:
    print((h-u)//(u-d)+1)








