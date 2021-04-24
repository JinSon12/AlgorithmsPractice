animals = ["ant", "bee", "cat", "dog"]

# Joining
print(",".join(animals))  # result => ant,bee,cat,dog


print("\n".join(animals))
# output
"""
ant
bee
cat
dog
"""

print("/".join(animals))


# Splitting
animalString = "/".join(animals)

animalSplit = animalString.split("/")
print(animalSplit)  # return ['ant', 'bee', 'cat', 'dog']
