def count_sort(arr):
    k = max(arr)
    output = [0 for _ in range(0,len(arr))]
    count_array = [0 for _ in range(0,k+1)]

    for i in range(0, len(arr)):
        count_array[arr[i]] += 1

    for i in range(1, k + 1):
        count_array[i] += count_array[i-1]

    for i in reversed(range(0, len(arr))):
        output[count_array[arr[i]] - 1] = arr[i]
        count_array[arr[i]] -= 1

    return output

if __name__ == "__main__":
    arr = [4, 2, 2, 5, 3, 3, 1]
    output = count_sort(arr)
    print(output)
