class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # Besides using random.shuffle from python, we can also use Fisher-Yates Algorithm:
        # For each index, we can choose the random swaping index after that index.
        index = [i for i in range(len(self.original))]
        random.shuffle(index)
        res = [self.original[x] for x in index]
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()