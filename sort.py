

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


def selection_sort(items):
    for i in range(0, len(items) - 1):
        min_index = i
        for a in range(i + 1, len(items)):
            if items[a] < items[min_index]:
                min_index = a
        if min_index != i:
            temp = items[min_index]
            items[min_index] = items[i]
            items[i] = temp
    return items


unsorted_list = [9,8,7,6,5,2,1,4]

print(selection_sort(unsorted_list))
