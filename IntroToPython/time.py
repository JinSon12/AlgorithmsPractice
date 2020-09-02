import time

input("press enter and count to 20")
start = time.time()

input("press enter again after 20 seconds")
end = time.time()

et = end - start
print("You pressed enter again after ", et, "seconds")
print("difference would be = ", abs(et-20), "seconds")
