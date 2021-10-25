import sys

input=sys.stdin.readline

a, b, c = map(int, input().split())

if b>c or b==c :
    print(-1)
    sys.exit()

ans=a/(c-b) + 1

print(int(ans))