num = int(input())
count = 0
while num != 1:
    if num%2 != 0:
        num = 3*num +1
    num = num // 2
    count = count + 1
    # print(num)
print(count)