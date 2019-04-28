class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if not intervals:
            return intervals
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
                