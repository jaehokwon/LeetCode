class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        dp = [0] * len(word)
        for i, v in enumerate(word):
            isVowel = v in vowels
            if i > 0:
                dp[i] = dp[i-1]*2
            if i > 1:
                dp[i] -= dp[i-2]
            if isVowel:
                dp[i] += i + 1

        return dp[-1]