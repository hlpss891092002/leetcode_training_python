def minEatingSpeed(piles, h) -> int:
        def counter(rate):
            count = 0
            for pile in piles:
                if pile % rate > 0:
                    count += pile // rate + 1
                else:
                    count += pile // rate
            return count
        max_pile = max(piles)
        min_pile = 1
        ans = 1
        while max_pile >= min_pile:
            mid_pile = (max_pile + min_pile)//2
            print(mid_pile)
            hrs = counter(mid_pile)
            if hrs > h:
                min_pile = mid_pile + 1 
            if hrs <= h:
                max_pile = mid_pile - 1
                ans =  mid_pile
            print(mid_pile)
        return ans
result = minEatingSpeed([312884470], 968709470)
print(result)
