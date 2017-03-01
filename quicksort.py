


def quick_sort(items, start, end):
    if start < end:
        wall = build_wall(items, start, end)
        # recusivly sort left
        quick_sort(items, start, wall - 1)
        # recursivly sort right
        quick_sort(items, wall + 1, end)
    return items

# Choses pivot and moves everything <pivot to left of wall
def build_wall(items, start, end):
    pivot = end
    pivot_value = items[pivot]
    wall = start

    for i in range(start, end):
        # If any value is less than the pivot, put it on the other side of the wall
        if items[i] < pivot_value:
            # swap
            items[i], items[wall] = items[wall], items[i]
            wall += 1
    items[pivot], items[wall] = items[wall], items[pivot]
    return wall



# Run - (This is my unit test)
data = [4,6,8,3,5,9,2]
print(quick_sort(data, 0, len(data) - 1))
