class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # Should current asteroid be in stack?
            alive = True
            while alive and (asteroid < 0) and stack and (stack[-1] > 0):
                # Collision occurs if this is true
                if (abs(asteroid) > stack[-1]):
                    stack.pop() # Top asteroid in stack blows up
                elif (abs(asteroid) == stack[-1]):
                    stack.pop()
                    alive = False
                else:
                    # Current asteroid blows up
                    alive = False
            if alive:
                stack.append(asteroid)
        return stack
