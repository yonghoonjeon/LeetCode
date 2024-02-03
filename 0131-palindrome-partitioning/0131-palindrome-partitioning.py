class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        
        output = []
        
        # 개수 별로 s길이 만큼 검사
        for i in range(len(s)):
            # check palindrome
            if self.is_palindrome(s[:i+1]):
                for sub in self.partition(s[i+1:]):  
                    output.append([s[:i+1]] + sub)
    
        return output
    
    def is_palindrome(self, s: str):
        return s == s[::-1]
                    