class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # We can use Sorting or Hash Set to solve this problem
        # Thought they are not meeting the requirement of non-modified and O(1) space
        # The right solution is following Floyd's theory from Linked List Cycle II
        
        # 68ms: 84.45%
        slow = fast = nums[0]
        # Phase 1:
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Phase 2:
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow