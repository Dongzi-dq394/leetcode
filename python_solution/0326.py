class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Solution 1: Recursively (72ms: 90%)
        
        if n<3: return n==1
        return n%3==0 and self.isPowerOfThree(n//3)
        
        # Solution 2: without any loop/recursion --> Logrithm (96ms: 47.41%)
        # threshold is hard to choose!!! from -6 to -12....
        if n<=0: return False
        temp = math.log(n, 3)
        print(temp)
        threshold = 1e-12
        return abs(int(temp)-temp) <= threshold or abs(int(temp)+1-temp) <= threshold
        
        # Solution 3: Mathematics from Solution take advantage of integer
        # 3^19 == 1162261467, which is the largest number in form 3^k less than 2^31-1
        return n>0 and 1162261467%n==0