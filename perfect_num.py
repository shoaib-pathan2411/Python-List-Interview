def find_perfect_num(num):
    sum1 = 0
    for i in range(1, num):
        if num % i == 0:
            sum1 += i
    if sum1 == num:
        return True
    else:
        return False

print(find_perfect_num(6)) # 1 2 3 = 6
print(find_perfect_num(28)) # 1 2 4 7 14 = 28
print(find_perfect_num(12)) # 1 2 3 4 6 = 16