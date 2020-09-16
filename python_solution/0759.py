"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        border = []
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                border.append((schedule[i][j].start, 0))
                border.append((schedule[i][j].end, 1))
        
        border.sort()
        res = []
        left = border[0][0]
        relax = 1
        for i in range(1, len(border)):
            if relax==0:
                res.append(Interval(left, border[i][0]))
            left = border[i][0]
            relax = relax+1 if border[i][1]==0 else relax-1
        return res