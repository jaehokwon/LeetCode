class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        len_word = len(word)

        def isVowel(c):
            return c in vowels

        if len_word == 0:
            return 0
        if len_word == 1:
            return int(isVowel(word))
        dp = [0] * len_word
        dp[0] = int(isVowel(word[0]))
        dp[1] = dp[0]*2 + int(isVowel(word[1]))*2

        for i in range(2, len_word):
            dp[i] = dp[i-1]*2 - dp[i-2]
            if isVowel(word[i]):
                dp[i] += i+1

        return dp[-1]