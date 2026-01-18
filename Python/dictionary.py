# Dictionaries are used to store data values in key value pairs
# Dictionary are mutable(no index), unordered, and dont allow duplicates keys

info = {
    9 : 100,
    "key" : "lost",
    "age" : 34,
    "is_adult" : True,
    "marks" : 56.9,
    "subjects" : ["C++", "java", "python"],
    "topics" : ("DBMS", "CN")
}

print(info)
print(info["subjects"])
info["key"] = "found"
print(info)

print(info.keys())

# typecast
print(list(info.keys()))

print(len(info))

print(info.values())


# returns all (key,val) pairs as tuples
print(info.items())

# set - collection of unordered items, must be unique and immutable and we acn store tuple in it
# sets are mutable but the elemnts in the sets are immutable
collection = {1,5,"world"}

# empty set
empty_set = set()

# # set functions
# collection.add(3)
# collection.remove(1)
# collection.clear()
# collection.pop()

# SET union and intersection
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))