class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(root, idx):
            if idx == len(word):
                return root.is_end

            if word[idx] in root.children:
                root = root.children[word[idx]]
                return dfs(root, idx + 1)

            if word[idx] == '.':
                for ch in root.children:
                    curr = root
                    root = root.children[ch]
                    if dfs(root, idx + 1):
                        return True
                    root = curr

            return False
            
        return dfs(curr, 0)
