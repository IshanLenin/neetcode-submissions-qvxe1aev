class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = []
        count = [0] * n

        for i in range(n):
            heapq.heappush(available, (0, i))

        for start, end in meetings:
            while available and available[0][0] < start:
                end_time, room = heapq.heappop(available)
                heapq.heappush(available, (start, room))

            end_time, room = heapq.heappop(available)
            heapq.heappush(available, (end_time + (end - start), room))
            count[room] += 1

        return count.index(max(count))