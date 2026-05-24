class Node:
    def __init__(self):
        self.trie=defaultdict(Node)
        self.end=False

class PrefixTree:

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        r=self.root
        for w in word:
            char_idx = ord(w)-ord('a')
            if char_idx not in r.trie:
                r.trie[char_idx]=Node()
            r=r.trie[char_idx]
        r.end=True

    def search(self, word: str) -> bool:
        r=self.root
        for w in word:
            char_idx = ord(w)-ord('a')
            if char_idx in r.trie:
                r=r.trie[char_idx]
            else:
                return False
        
        return r.end

        

    def startsWith(self, prefix: str) -> bool:
        r=self.root
        for w in prefix:
            char_idx = ord(w)-ord('a')
            if char_idx in r.trie:
                r=r.trie[char_idx]
            else:
                return False
        
        return True
