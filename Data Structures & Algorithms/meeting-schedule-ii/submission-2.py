"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x:x.start)

        pq = []
        # heapq.heappush(pq, intervals[0].end)
        rooms = 0
        for i in intervals:
            if(pq and pq[0] <= i.start):
                heapq.heappop(pq)
            else:
                rooms += 1
            heapq.heappush(pq, i.end)

        return rooms
