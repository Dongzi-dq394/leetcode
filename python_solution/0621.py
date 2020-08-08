class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Solution 1: Greedy from discussion (412ms: 95.22%)
        if not tasks: return 0
        count = Counter(tasks)
        ele = list(count.values())
        ele.sort(reverse=True)
        number = ele[0]
        i = 1
        while i<len(ele) and ele[i] == ele[0]:
            i += 1
        return max(len(tasks), (number-1)*(n+1)+i)