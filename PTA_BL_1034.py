inputArr = input().split()
# inputArr = "2/3 -4/2".split()

from fractions import Fraction
A1, A2 = map(int, inputArr[0].split("/"))
B1, B2 = map(int, inputArr[1].split("/"))
f1 = Fraction(A1, A2)
f2 = Fraction(B1, B2)
def format1(num):

    if '/' not in str(num) or abs(num)<1:
        if num<0:
            num = '('+ str(num)+')'
        return num
    else:
        n1, n2 = map(int, str(abs(num)).split('/'))
        if num < 0:
            res = '(-' + str(n1//n2) + ' ' + str(n1%n2)+'/'+str(n2)+')'
        else:
            res = str(n1 // n2) + ' ' + str(n1 % n2) + '/' + str(n2)
        return res
print('{} + {} = {}'.format(format1(f1), format1(f2), format1(f1+f2)))
print('{} - {} = {}'.format(format1(f1), format1(f2), format1(f1-f2)))
print('{} * {} = {}'.format(format1(f1), format1(f2), format1(f1*f2)))
if f2 == 0:
    print("{} / {} = {}".format(format1(f1), format1(f2), "Inf"))
else:
    print("{} / {} = {}".format(format1(f1), format1(f2), format1(f1/f2)))