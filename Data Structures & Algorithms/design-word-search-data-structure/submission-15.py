class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for i, c in enumerate(word):
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.isWord = True

    def search(self, word: str) -> bool:

        def dfs(node, i):

            if i == len(word):
                return node.isWord

            c = word[i]

            if c == '.':
                for value in node.children.values():
                    if dfs(value, i+1):
                        return True

                return False

            if c not in node.children:
                return False

            return dfs(node.children[c], i+1)

        return dfs(self.root, 0)


        