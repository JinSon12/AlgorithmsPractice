import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random_set = dict({})
        self.set_arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        in_set = False
        if val not in self.random_set:
            self.set_arr.append(val)
            self.random_set[val] = len(self.set_arr) - 1
            in_set = True

        return in_set

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # print(self.random_set)
        in_set = False
        if val in self.random_set:
            in_set = True
            ind_to_del = self.random_set[val]
            self.random_set.pop(val)
            # print( ind_to_del)
            if len(self.set_arr) > 1:
                el_to_swap = self.set_arr[len(self.set_arr) - 1]
                self.set_arr.pop()

                # updating the swapped element's position information in the set.
                self.random_set[el_to_swap] = ind_to_del
            else:
                self.set_arr.pop()

        return in_set

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        print(self.set_arr, self.random_set)
        length = len(self.random_set)
        rand_num = random.randint(0, length-1)

        return self.set_arr[rand_num]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
