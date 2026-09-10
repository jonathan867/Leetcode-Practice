# trie: a tree of nodes representing each char. nodes have children and an end t/f

class Node:
    def __init__(self):
        self.children = {} # dict of next nodes: char -> Node
        self.end = False # denotes if this node is the end of an existing word

class Trie:
    

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curNode = self.root

        for c in word:
            if c not in curNode.children: # keep following the path, make a new path if not already there
                curNode.children[c] = Node()
            curNode = curNode.children[c]
        
        # mark the end of the new word
        curNode.end = True


    def search(self, word: str) -> bool:
        curNode = self.root

        for c in word:
            if c not in curNode.children: # keep following the path
                return False
            curNode = curNode.children[c]
        return curNode.end
        

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root

        for c in prefix:
            if c not in curNode.children: # keep following the path
                return False
            curNode = curNode.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)