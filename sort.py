

def bubble_sort(items):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(items) - 1):
            if items[i] > items[i + 1]:
                is_sorted = False
                temp = items[i]
                items[i] = items[i + 1]
                items[i + 1] = temp
    return items

unsorted_list = [9,8,7,6,5,2,1,4]

print(bubble_sort(unsorted_list))
