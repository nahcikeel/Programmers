n = int(input())
num = n
cnt=0 

while True:
    a = num // 10
    b = num % 10
    c = (a+b) % 10

    cnt += 1

    num = b*10+c

    if num == n:
        break

print(cnt)