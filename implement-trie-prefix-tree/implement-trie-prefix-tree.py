class TrieNode:
    def __init__(self):
        self.childs = {}
        self.endWord = False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        crawl = self.root
        
        for c in word:
            if c not in crawl.childs:
                crawl.childs[c] = TrieNode()
            crawl = crawl.childs[c]
        
        crawl.endWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        crawl = self.root
        
        for c in word:
            if c not in crawl.childs:
                return False
            crawl = crawl.childs[c]
        
        return crawl.endWord
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        crawl = self.root
        
        index = 0
        while index < len(prefix):
            c = prefix[index]
            if c not in crawl.childs:
                return False
            crawl = crawl.childs[c]
            index += 1
        
        return index >= len(prefix)
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)