inputCount = int(input())
# inputCount = int("4")
for i in range(inputCount):
    A, B, C = map(int, input().split())
    # A, B, C = map(int, "0 -2147483648 -2147483647".split())
    if (A + B) > C:
        print("Case #"+ str(i+1) +": true")
    else:
        print("Case #" + str(i + 1) + ": false")
