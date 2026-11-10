def swap_variables(a,b):
    a,b = b,a # 5,10 -> 10,5
    return a,b
print(swap_variables(5,10))

def swap_variables_without_temp(a,b):
    a = a + b # 5+10 = 15
    b = a - b # 15-10 = 5
    a = a - b # 15-5 = 10
    return a,b
print(swap_variables_without_temp(5,10))

def swap_variables_with_temp(a,b):
    temp = a # 5
    a = b # 10
    b = temp # 5
    return a,b
print(swap_variables_with_temp(5,10))