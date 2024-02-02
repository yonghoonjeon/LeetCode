class MyHashSet:

    def __init__(self):
        self.key_set = [0 for _ in range(1000001)]
    
    def add(self, key: int) -> None:
        self.key_set[key] = 1
        

    def remove(self, key: int) -> None:
        self.key_set[key] = 0

    def contains(self, key: int) -> bool:
        return True if self.key_set[key] else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)