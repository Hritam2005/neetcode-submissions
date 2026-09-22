class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {};result = []
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        for n in sorted(count, key=count.get, reverse=True):
            result.append(n)

            if len(result) == k:
                break

        return result