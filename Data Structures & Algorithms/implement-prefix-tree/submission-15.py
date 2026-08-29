class PrefixTree:

    def __init__(self):
        self.prefix = collections.defaultdict(dict)
        self.word_set = set()

    def insert(self, word: str) -> None:
        obj = self.prefix
        for c in word:
            if c not in obj:
                obj[c] = {}
            obj = obj.get(c)

        self.word_set.add(word)

    def search(self, word: str) -> bool:
        return word in self.word_set

    def startsWith(self, prefix: str) -> bool:
        obj = self.prefix
        for c in prefix:
            if c not in obj:
                return False
            obj = obj.get(c)
        
        return True
        