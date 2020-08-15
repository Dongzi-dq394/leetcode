class Solution:
    # This is for the second solution, we pre-compute the whole array.
    ugly = sorted(2**a * 3**b * 5**c for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber(self, n: int) -> int:
        # Solution 1: from discussion: big ugly number comes from smaller one (196ms: 67.22%)
        arr = [1]
        index_2 = index_3 = index_5 = 0
        for i in range(1, n):
            threshold = arr[i-1]
            while arr[index_2]*2<=threshold:
                index_2 += 1
            while arr[index_3]*3<=threshold:
                index_3 += 1
            while arr[index_5]*5<=threshold:
                index_5 += 1
            arr.append(min(arr[index_2]*2, arr[index_3]*3, arr[index_5]*5))
        return arr[-1]
        
        # Solution 2: from discussion (36ms: 98.26%)
        # If we compute at here for each time, the running time will be much longer
        #ugly = sorted(2**a * 3**b * 5**c for a in range(32) for b in range(20) for c in range(14))
        return self.ugly[n-1]