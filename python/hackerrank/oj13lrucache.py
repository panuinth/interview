class LRUCache:
    
    # @param capacity, an integer
    def __init__(self, capacity):
        self.l = list()
        self.d = dict()
        self.c = capacity
        
    # @return an integer
    def get(self, key):
        if key not in self.d:
            return -1
        else:
            self.l.remove(key)
            self.l.insert(0, key)
            return self.d.get(key, -1)
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.d:
            self.d[key] = value
            self.l.insert(0, key)
            if len(self.l) > self.c:
                x = self.l.pop()
                del self.d[x]
        else:
            self.d[key] = value
            self.l.remove(key)
            self.l.insert(0, key)


def test():
    l = LRUCache(5)
    for i in range(100):
        l.get(2)
        l.set(i, i)
    print l.l


test()
