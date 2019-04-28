class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        for index in range(1, len(intervals)):
            if intervals[index][0] > end:
                res.append([start, end])
                start = intervals[index][0]
                end = intervals[index][1]
            else:
                end = max(end, intervals[index][1])
        res.append([start, end])
        return res