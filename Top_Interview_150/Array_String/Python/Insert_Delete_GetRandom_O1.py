import random
class RandomizedSet:

    def __init__(self):
        self.nums = [] # List to store elements
        self.val_to_index = {} # Dictionary storing value to index

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        idx_to_remove = self.val_to_index[val]
        self.nums[idx_to_remove] = self.nums[-1]
        self.val_to_index[self.nums[-1]] = idx_to_remove
        self.nums.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
