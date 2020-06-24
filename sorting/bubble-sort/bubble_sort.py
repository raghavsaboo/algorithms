def bubble_sort(arr):
    last_unsorted_index = len(arr) - 1
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(0, last_unsorted_index):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        last_unsorted_index -= 1

if __name__ == "__main__":
    arr = [1, 10, 2, 20, 5]
    bubble_sort(arr)
    print(arr)