class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flow_len = len(flowerbed)
        viable_count = 0
        if n==0:
            return True
        for i in range(flow_len):
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == flow_len-1 or flowerbed[i+1] == 0)):
                # Mark spot as occupied
                flowerbed[i] = 1
                # Add to viable count
                viable_count += 1
        if viable_count >= n:
            return True
        else: return False