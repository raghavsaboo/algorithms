# Tries

## Trie Implementation

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.trie
        for char in word:
            if char in current:
                current = current[char]
            else:
                current[char] = dict()
                current = current[char]
        current['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.trie
        for char in word:
            try:
                current = current[char]
            except KeyError:
                return False
        if '#' in current:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.trie
        for char in prefix:
            try:
                current = current[char]
            except KeyError:
                return False
        
        if len(current) > 0:
            return True
        else:
            return False
        
```

## Implement Autocomplete System

>Given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
>
>```python
>class Trie:
>    ...
>    
>    def find(self, prefix: str) -> list:
>        trie = self.trie
>        for char in prefix:
>            if char in trie:
>                trie = trie[char]
>            else:
>                return []
>        return self._elements(trie)
>    
>    def _elements(self, d):
>        result = []
>        for c, v in d.items():
>            if c == "#":
>                subresult = ['']
>            else:
>                subresult = [c + s for s in self._elements(v)]
>            result.extend(subresult)
>         return result
>    
>def autocomplete(s):
>    suffixes = trie.find(s)
>    return [s + w for w in suffixes]
>
>trie = Trie()
>for word in words:
>    trie.insert(word)
>```
>
>