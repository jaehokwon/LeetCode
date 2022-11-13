class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dic = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'],
               '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'],
               '8': ['t','u','v'], '9': ['w','x','y','z']}
        lst = dic[digits[0]].copy()
        for i, n in enumerate(digits):
            if i==0:
                continue
            for j in range(0, len(lst)):
                cur = lst.pop(0)
                for k in dic[n]:
                    lst.append(cur + k)
            
        return lst