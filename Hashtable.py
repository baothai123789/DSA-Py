class Hashtable:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None

    def __init__(self, size):
        self._data = [None] * 10
        self.size = size
        self.LOAD_FACTOR = 0.75

    def push(self, key, val):
        newone = Hashtable.Node(key, val)
        hash_val = hash(key) % self.size
        newone.next = self._data[hash_val]
        self._data[hash_val] = newone

    def get(self, key, defaultval=None):
        hash_val = hash(key) % self.size
        if not self._data[hash_val]:
            return defaultval
        cur = self._data[hash_val]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return defaultval

    def __repr__(self):
        ans = ""
        for ele in self._data:
            if ele:
                ans += f"{ele.key}:{ele.val} "
        return f"Map({ans})"


def main():
    map1 = Hashtable(10)
    map1.push("Bao", 1)
    print(map1)


if __name__ == '__main__':
    main()
