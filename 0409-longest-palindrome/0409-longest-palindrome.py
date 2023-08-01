class Solution:
    def longestPalindrome(self, s: str) -> int:
        import collections
        
        freq_cnt = collections.Counter(s)
        is_odd = 0
        
        for character, count in freq_cnt.items():
            if count % 2 == 1:
                freq_cnt[character] = count - 1
                is_odd = 1
        
        return sum(list(freq_cnt.values())) + is_odd