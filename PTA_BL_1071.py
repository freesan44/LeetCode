money, round = map(int, input().split(" "))
# money, round = map(int, "100 4".split(" "))
for i in range(round):
    n1, b , t, n2 = map(int, input().split(" "))
    # n1, b, t, n2 = map(int, "8 0 100 2".split(" "))
    if t > money:
        print("Not enough tokens.  Total = "+str(money)+".")
        continue
    if (n1 > n2 and b == 0) or  (n1 < n2 and b == 1):
        #赢了
        money = money + t
        print("Win "+str(t)+"!  Total = "+str(money)+".")
    else:
        #输了
        money = money - t
        print("Lose "+str(t)+".  Total = "+str(money)+".")
        if money == 0:
            print("Game Over.")
            break

