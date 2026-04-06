class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        out = []

        # Hash table where key-value: num-freq
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        # print(freq)

        # Sort table based on freq
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # print(sorted_items)

        # Select top k freq elements
        for i in range(0, k):
            out.append(sorted_items[i][0])
        
        return out
        