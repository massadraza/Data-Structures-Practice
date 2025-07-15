# Learning how to implement a hash set in python

class HashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size
    
    def add(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket
    
    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        print("Hash Set Contents:")
        for index, bucket, in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")

newHashVar = HashSet(size=10)

newHashVar.add("Bob")

newHashVar.print_set()