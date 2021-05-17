from collections import defaultdict

Dict = {1: 'shin ramyeon', 2: 'jin ramyeon', 3: 'buldak'}
print("Ramyeon Dictionary")
print(Dict)
print(Dict[1])

# Below line generates a key error
# print(Dict[5])

# Using DefaultDict, we can prevent key error
ramenDict = defaultdict(str)
ramenDict[1] = "shoyu ramen"
ramenDict[2] = "tonkotsu ramen"
ramenDict[3] = "tantanmen"

# prints empty string
print(ramenDict[5])

# alternatively, we can use lambda fn.
pizzaDict = defaultdict(lambda: 'cheese pizza')
pizzaDict[1] = "pepperoni pizza"

# prints cheese pizza
print(pizzaDict[2])
