def find_max_product_pair(list1):
    # Track the indices of the pair with the greatest product.
    a = 0
    b = 1
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            # Replace the current pair when a larger product is found.
            if list1[i] * list1[j] > list1[a] * list1[b]:
                a = i
                b = j
    # return (a, b)
    return (a, b)
 
print(find_max_product_pair([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def find_max_product_pair(list1):
    # Start with the first two values as the best pair found so far.
    a = list1[0]
    b = list1[1]
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            # Keep the values of the pair with the greatest product.
            if list1[i] * list1[j] > a * b:
                a = list1[i]
                b = list1[j]
    # return (a, b)
    return a, b

print(find_max_product_pair([1, 2, 3, 4, 5, 6, 7, 8, 9]))