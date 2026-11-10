def iterate_list_without_using_loop(lst, pos):
    if pos < len(lst):
        print(lst[pos])
        iterate_list_without_using_loop(lst, pos + 1)

iterate_list_without_using_loop([1, 2, 3, 4, 5, 6, 7, 8, 9], 0)        