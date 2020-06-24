def partition(arr, p, q):
    x = arr[p]
    i = p
    for j in range(p+1, q+1):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[i] = arr[i], arr[p]
    return i

def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)

if __name__ == "__main__":
    arr = [54, 26, 93, 17, 77, 31, 44, 55]
    quick_sort(arr, 0, len(arr) -1)
    print(arr)