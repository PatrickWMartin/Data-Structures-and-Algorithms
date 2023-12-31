# A toy hashmap implementation to show the basics of how
# a hashmap works under the hood
class HashMap:
    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for ch in key:
            sum += ord(key)

        return sum % len(self.hashmap)

    def insert(self, key, value):
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        value = self.hashmap[index]
        if value is None:
            raise Exception("Key not found")
        return value[1]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v is not None:
                buckets.append(v)
        return str(buckets)
