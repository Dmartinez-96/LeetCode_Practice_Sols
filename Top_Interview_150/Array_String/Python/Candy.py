class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings) # Each kid gets a candy at least
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                # Child has higher rating than left-neighbor, should have more candy
                candies[i] = candies[i - 1] + 1
        
        # Pass back through in reverse to check rating condition
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # Child has higher rating than right-neighbor, should have more candy
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        total_candies = sum(candies)
        return total_candies
