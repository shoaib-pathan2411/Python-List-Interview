def find_armstrong_num():
    for i in range(1, 501):
        num = i
        n = len(str(i))
        sum1 = 0
        i = str(i)
        for digit in i:
            sum1 = sum1 + int(digit) ** n
        if sum1 == num:
            print(num)
find_armstrong_num()

def is_armstrong_num(num):
    temp = num
    n = len(str(num))
    sum1 = 0
    digits = str(num)
    for digit in digits:
        sum1 = sum1 + int(digit) ** n
    return sum1 == num

print(is_armstrong_num(154))
print(is_armstrong_num(153))