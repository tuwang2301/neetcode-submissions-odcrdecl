class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        print(self.dic)
        arr = self.dic.get(key, [])

        l, r = 0, len(arr) - 1
        prev = ""
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                prev = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return prev
