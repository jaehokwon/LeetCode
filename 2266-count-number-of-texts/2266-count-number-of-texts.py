class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        if len(pressedKeys) == 1:
            return 1
        dic = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'],
               '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'],
               '8': ['t','u','v'], '9': ['w','x','y','z']}
        dp = [0] * (len(pressedKeys) + 0)
        dp[0] = 1 # 0
        dp[1] = 2 if pressedKeys[0] == pressedKeys[1] else 1 # 1
        cnt = dp[1]
        modulo = pow(10, 9) + 7
        for i in range(2, len(pressedKeys) + 0):
            if pressedKeys[i] == pressedKeys[i-1]:
                cnt += 1
                
                if cnt <= len(dic[pressedKeys[i]]):
                    dp[i] += dp[i-1]*2
                else:
                    for j in range(1, len(dic[pressedKeys[i]]) + 1):
                        dp[i] += dp[i-j]
            else:
                cnt = 1
                dp[i] += dp[i-1]
        
        return dp[-1] % modulo