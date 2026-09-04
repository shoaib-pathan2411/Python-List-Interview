# Sort a List (Without Built-in) – with Bubble Sort
def bubble_sort(lst):
    for i in range(len(lst)):
        print("this is outer loop")
        print(i)
        for j in range(len(lst)-1):
            print("this is inner loop")
            print(j)
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

print(bubble_sort([5, 2,4,5,3,5,7,4,2,5,78,9,5, 9, 1]))