import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        pq = []
        for num, freq in counts.items():
            heapq.heappush(pq, (-freq, num))
        
        out = []
        for _ in range(k):
            freq, num = heapq.heappop(pq)
            out.append(num)
        return out