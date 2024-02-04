class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        import collections
        
        # false condition
        if len(s) < k:
            return False
        # character counter
        c_count = collections.Counter(s)
        # declare odd counts
        odd_count = 0
        # odd count check
        for key, v in c_count.items():
            # if odds
            if v%2 != 0:
                # update odds count
                odd_count += 1
        
        # false condition
        if odd_count > k:
            return False
        
        return True