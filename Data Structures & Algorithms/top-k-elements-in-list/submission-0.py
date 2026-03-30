import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        data = []
        for key, value in count.items():
            heapq.heappush(data, (-value, key))
        
        res = []
        while len(res) != k:
            _, num = heapq.heappop(data)
            res.append(num)
        
        return res