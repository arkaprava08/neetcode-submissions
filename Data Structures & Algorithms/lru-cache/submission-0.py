class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.left=None
        self.right=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size=0
        self.left=Node(-1, -1)
        self.right=Node(-1, -1)
        self.left.right=self.right
        self.right.left=self.left
        self.valmap={}

    def insert(self, node):
        tmp=self.left.right
        self.left.right=node
        node.left=self.left
        tmp.left=node
        node.right=tmp
        self.size+=1
    
    def delete(self, node):
        node.left.right=node.right
        node.right.left=node.left
        self.size-=1


    def get(self, key: int) -> int:
        if key in self.valmap:
            out=self.valmap[key]
            self.delete(out)
            self.insert(out)
            return out.val
        
        return -1

        

    def put(self, key: int, value: int) -> None:

        if key in self.valmap:
            self.delete(self.valmap[key])
        
        node=Node(key, value)
        self.valmap[key]=node
        self.insert(node)


        if self.size > self.capacity:
            node=self.right.left
            self.delete(node)
            del(self.valmap[node.key])
        
