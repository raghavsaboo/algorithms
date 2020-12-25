# Binary Search Trees

## BST Implementation

```python
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, x):
        if not self.root:
            self.root = Node(x)
        else:
            self._insert(x, self.root)
            
     def _insert(self, x, root):
        if x < root.data:
            if not root.left:
                root.left = Node(x)
            else:
                self.insert(x, root.left)
         else:
            if not root.right:
                root.right = Node(x)
            else:
                self.insert(x, root.right)
      
       def find(self, x):
            if not self.root:
                return False
            else:
                return self._find(x, self.root)
       
       def _find(self, x, root):
            if not root:
                return False
            elif x == root.data:
                return True
            elif x < root.data:
                return self._find(x, root.left)
            else:
                return self._find(x, root.right)
```

## Find Floor and Ceiling

>Given a binary search tree, find the floor and ceiling of a given integer. The floor is the highest element in the tree less than or equal to an integer, while the ceiling is the lowest element in the tree greater than or equal to an integer.
>
>### Solution
>
>```python
>class Node:
>    def __init__(self, data, left=None, right=None):
>        self.data = data
>        self.left = left
>        self.right = right
>        
>def get_bounds(root, x, floor=None, ceil=None):
>    if not root:
>        return floor, ceil
>    
>    if x == root.data:
>        return x, x
>    
>    elif x < root.data:
>        floor, ceil = get_bounds(root.left, x, floor, root.data)
>    
>    else:
>        floor, ceil = get_bounds(root.right, x, root.data, ceil)
>        
>    return floor, ceil
>```

## Convert Sorted Array to BST

>Given a sorted array, convert it into a height-balanced binary search tree.
>
>### Solution
>
>```python
>def make_bst(array):
>    if not array:
>        return None
>    
>    mid = len(array) // 2
>    
>    root = Node(array[mid])
>    root.left = make_bst(array[:mid])
>    root.right = make_bst(array[mid+1:])
>    
>    return root
>```

# Red Black Trees

# AVL Trees

