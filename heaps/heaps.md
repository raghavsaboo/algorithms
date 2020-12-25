# Heaps

## Compute the Running Median

>Given a sequence of numbers, compute the running median as new elements are added.
>
>```python
># Example 1
>> running_median([2, 1, 5, 7, 2, 0, 5])
>> [2, 1.5, 2, 3.5, 2, 2, 2]
>```
>
>### Solution
>
>```python
>import heapq
>
>def get_median(min_heap, max_heap):
>    if len(min_heap) > len(max_heap):
>        min_val = heapq.heappop(min_heap)
>        heapq.heappush(min_heap, min_val)
>    	return min_val
>	elif len(min_heap) < len(max_heap):
>        max_val = heapq.heappop(max_heap)
>        heapq.heappush(max_heap, max_val)
>        return max_val
>    else:
>        min_val = heapq.heappop(min_heap)
>        heapq.heappush(min_heap, min_val)
>        max_val = heapq.heappop(max_heap)
>        heapq.heappush(max_heap, max_val)
>        return (min_val + max_val) / 2
>    
>def add(num, min_heap, max_heap):
>    # If empty, then just add it to the max heap
>    if len(min_heap) + len(max_heap) <= 1:
>        heapq.heappush(max_heap, num)
>        return
>    
>    median = get_median(min_heap, max_heap)
>    if num > median:
>        # add it to the min heap
>        heapq.heappush(min_heap, num)
>    else:
>        heapq.heappush(max_heap, num)
>        
>def rebalance(min_heap, max_heap):
>    if len(min_heap) > len(max_heap) + 1:
>        root = heapq.heappop(min_heap)
>        heapq.heappush(max_heap, root)
>    elif len(max_heap) > len(min_eap) + 1:
>        root = heapq.heappop(max_heap)
>        heapq.heappush(min_heap, root)
>        
> def running_median(stream):
>    min_heap = []
>    max_heap = []
>    output = []
>    for num in stream:
>        add(num, min_heap, max_heap)
>        rebalance(min_heap, max_heap)
>        median_val = get_median(min_heap, max_heap)
>        output.append(median_val)
>        
>    return output
>```

## Huffman Encoding / Tree

## Examples

