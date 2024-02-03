class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        ref: https://leo-bb.tistory.com/14
        """
        # 문자열이 공백인 경우 그대로 출력
        if len(s)==0:
            return s
        # 현재까지 발견한 가장 긴 팰린드롬 부분 문자열의 길이    
        maxLen=1
        # 현재까지 발견한 가장 긴 팰린드롬 부분 문자열의 시작 인덱스
        start=0

        # 문자열이 공백이 아닌 경우 우측으로 한 칸씩 움직이며 팰린드롬의 조건을 탐색
        for i in range(len(s)):
            # 현재 문자열을 중심으로 하는 홀수 길이의 팰린드롬을 검사
            if i - maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen += 2
                continue
            # 현재 문자열과 오른쪽에 위치한 문자를 중심으로 하는 짝수 길이의 팰린드롬을 검사
            if i - maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen += 1
                
        # 가장 긴 팰린드롬 부분 문자열을 반환
        return s[start:start+maxLen]