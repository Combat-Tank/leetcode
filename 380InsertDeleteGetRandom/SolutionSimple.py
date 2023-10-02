import random

class RandomizedSet:

    def __init__(self):
        self.value_list = []

    def insert(self, val: int) -> bool:
        for elem in self.value_list:
            if elem == val:
                return False

        return True        

    def remove(self, val: int) -> bool:
        for elem in self.value_list:
            if elem == val:
                self.value_list.remove(val)
                return True
        return False

    def getRandom(self) -> int:
        index = random.randint(0,len(self.value_list))
        
        return self.value_list[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()