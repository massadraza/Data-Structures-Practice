# Learning how to implement a hash table in python

hashData = [
    
    [None],
    ['Massad'],
    [None],
    ['Robert'],
    [None],
    ['Max'],
    [None], 
    ['Bob']
    
    ]

def hash_function(value):
    return sum(ord(char) for char in value) % 10

print("'a' has hash code:", hash_function('a'))

def add(value):
    index = hash_function(value)
    bucket = hashData[index]
    if value not in bucket:
        bucket.append(value)

def contains(value):
    index = hash_function(value)
    bucket = hashData[index]
    return value in bucket

print("'Massad' is in the Hash Set: ", hash_function('Massad'))

add('Joesph')

print(hashData)
print('Contains Joesph:', contains('Joesph'))

