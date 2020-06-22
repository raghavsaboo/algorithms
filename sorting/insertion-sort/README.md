# 1. ⎀ Insertion Sort

- [1. ⎀ Insertion Sort](#1--insertion-sort)
  - [1.1. Properties](#11-properties)
  - [1.2. Pseudo Code](#12-pseudo-code)
  - [1.3. Python Code](#13-python-code)
  - [1.4. Asymptotic Analysis](#14-asymptotic-analysis)
    - [1.4.1. Time Complexity](#141-time-complexity)
    - [1.4.2. Time Complexity](#142-time-complexity)

## 1.1. Properties
| Online | In-Place | Stable |
| ------ | -------- | ------ |
| ✓      | ✓        | ✓      |

## 1.2. Pseudo Code
![Wikimedia Animation](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)
```
for i in 2 to A.length {
    key = A[i]
    j = i - 1

    while j > 0 AND A[j] > key {
        A[j + 1] = A[j]
        j = j -1
    }
    A[j + 1] = key
}
```

## 1.3. Python Code
```python
def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while (j >= 0) and (arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
```

## 1.4. Asymptotic Analysis

| Complexity | Time     | Space  |
| ---------- | -------- | ------ |
| worst      | $O(n^2)$ | $O(1)$ |
| best       | $O(n)$   | $O(1)$ |

### 1.4.1. Time Complexity

| Line of Code                         | Best Case | Worst Case |
| ------------------------------------ | --------- | ---------- |
| ```python def insertion_sort(arr)``` | NA        | NA         |
| `for i in range(1, len(arr)):`       | $n$       | $n$        |
| `>> key = arr[i]`                    | $n-1$     | $n-1$      |
| `>> j = i -1`                        | $n-1$     | $n-1$      |
| `while (j>=0) and (arr[j] > key):`   | $n-1$     | $\frac{n(n+1)}{2}$ |
| `>> arr[j + 1] = arr[j]`             | $0$       | $\frac{n(n-1)}{2}$ |
| `>> j -= 1`                          | $0$       | $\frac{n(n-1)}{2}$ |
| `arr[j + 1] = key`                   | $n-1$     | $n-1$      |

### 1.4.2. Time Complexity
| Line of Code                         | Best Case | Worst Case |
| ------------------------------------ | --------- | ---------- |
| ```python def insertion_sort(arr)``` | NA        | NA         |
| `for i in range(1, len(arr)):`       | $1$       | $1$        |
| `>> key = arr[i]`                    | $1$       | $1$        |
| `>> j = i -1`                        | $1$       | $1$        |
| `while (j>=0) and (arr[j] > key):`   | NA        | NA         |
| `>> arr[j + 1] = arr[j]`             | NA        | NA         |
| `>> j -= 1`                          | NA        | NA         |
| `arr[j + 1] = key`                   | NA        | NA         |