class PrefixTree:

    def __init__(self):
        self.prefix = collections.defaultdict(dict)

    def insert(self, word: str) -> None:
        obj = self.prefix
        for c in word:
            if c not in obj:
                obj[c] = {}
            obj = obj.get(c)

        obj['#'] = True

    def search(self, word: str) -> bool:
        obj = self.prefix
        for c in word:
            if c not in obj:
                return False
            obj = obj.get(c)
        
        return '#' in obj

    def startsWith(self, prefix: str) -> bool:
        obj = self.prefix
        for c in prefix:
            if c not in obj:
                return False
            obj = obj.get(c)
        
        return True
        