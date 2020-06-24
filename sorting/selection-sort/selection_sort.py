def selection_sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]

if __name__ == "__main__":
    arr = [10, 1, 5, 20, 3]
    selection_sort(arr)
    print(arr)