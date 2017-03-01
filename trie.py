
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.data = None

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, value):
        current_node = self.root
        for i in range(0, len(key)):
            char = key[i]
            node = current_node.children.get(char)
            if node is None:
                node = TrieNode()
                current_node.children[char] = node
            current_node = node
        current_node.data = value

    def search(self, key):
        current_node = self.root
        for i in range(0, len(key)):
            char = key[i]
            node = current_node.children.get(char)
            if node is None:
                return None
            current_node = node
        return current_node.data



myTrie = Trie()
myTrie.insert("four", 4)
myTrie.insert("seven", 7)
myTrie.insert("six", 6)

print(myTrie.search("six"))
print(myTrie.search("seven"))
