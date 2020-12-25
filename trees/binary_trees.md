# Trees

## Reconstruct Binary Tree

### Using Pre-Order and In-Order Traversals

>Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
>
>```bash
># Example 1
>> generate_bt(inorder=[d,b,e,a,f,c,g], preorder=[a,b,d,e,c,f,g])
>
>		a
>	/		\
>   b		 c
> /	 \     /   \
>d     e   f     g
>```
>
>#### Solution
>
>```python
>def generate_bt(inorder, preorder):
>    if not preorder and not inorder:
>        return None
>    
>    if len(preorder) == len(inorder) == 1:
>        return preorder[0]
>    
>    # assume elements of the list are Tree Nodes
>    root = preorder[0]
>    root_i = inorder.index(root)
>    root.left = generate_bt(inorder[0:root_i], preorder[1:1+root_i])
>    root.right = generate_bt(inorder[root_i + 1:], preorder[1+root_i:])
>    
>    return root
>```

## Evaluate Arithmetic Tree

> Given an arithmetic binary tree with internal nodes that store arithmetic operations `+, -, *, /` and leaf nodes that store values, return the computed result.
>
> ```bash
> 		*
> 	/		\
>    +         +
>  /   \      /  \
> 3     2    4    5
> > 45
> ```
>
>  #### Solution
>
> ```python
> def compute(root):
>     if root.data.isnumeric():
>         return root.data
>     else:
>         return eval(str(compute(root.left)) + str(root.data) + str(root.right))
> ```

## Get Level with Minimum Sum

>Given a binary tree, return the level of the tree that has the minimum sum.
>
>```bash
>		1
>	/		\
>   2		 3
>           /   \
>          4     5
>> 0
>```
>
>#### Solution
>
>```python
>from collections import deque, defaultdict
>
>def minimum_sum_level(root):
>    queue = deque()
>    queue.append((root, 0))
>    
>    level_to_sum = defaultdict(int)
>    
>    while queue:
>        node, level = queue.popleft()
>        level_to_sum[level] += node.data
>        
>        if node.right:
>            queue.append((node.right, level + 1))
>        if node.left:
>            queue.append((node.left, level + 1))
>            
>	return min(level_to_sum, key=level_to_sum.get)
>```