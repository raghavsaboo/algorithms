# Disjoin-Set Data Structure

## Motivation

A classroom consists of `n` students whose friendships can be represented in an adjacency list as shown below:

```python
{
    0: [1, 2],
    1: [0, 5],
    2: [0],
    3: [6],
    4: [0],
    5: [1],
    6: [3]
}
```

Each student can be placed in a friend group, defined as the ==transitive closure== of that student's friendship relationships. i.e. **smallest set** such that no student in the group has any friends outside this group.

For the example above it would be `{0, 1, 2, 5}, {3, 6}, {4}`

## Description

This data structure needs to main methods:

- `union`
- `find`

### Algorithm

- Each student will is placed in a set consisting of only that student
- For each friendship in the input graph, we call our `union` method to place two students in the same set by:
  - calling `find` to get which friend group each student is in
  - if they are not in the same group, assign one of the students to the friend group of another
- In order to reduce the time complexity from $O(n)$ to $O(1)$ for the `find` call we do two things:
  - **path compression** - after we all `find` we know which group the student belongs to, so we can reassign this student directly to that group
  - **unite to larger** - assign the student belonging to the smaller set to the larger set

```python
class DisjointSet:
    def __init__(self, n):
        self.sets = list(range(n))
        self.sizes = [1] * n
        self.count = n
        
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            # Union by size: always add students to the bigger set
            if self.sizes[x] < self.sizes[y]:
                x, y = y, x
            self.sets[y] = x
            self.sizes[x] += self.sizes[y]
            self.count -= 1
            
    def find(self, x):
        group = self.sets[x]
        
        while group != self.sets[group]:
            group = self.sets[group]
            
        # Path compression: reassign x to the correct group
        self.sets[x] = group
        
        return group
    
def friend_groups(students):
    groups = DisjoinSet(len(students))
    
    for student, friends in students.items():
        for friend in friends:
            groups.union(student, friend)
            
    return groups.count
```

