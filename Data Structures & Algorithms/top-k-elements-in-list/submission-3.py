class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            result[num] = result.get(num, 0) + 1

        sorted_dict = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
        return list(sorted_dict.keys())[:k] 