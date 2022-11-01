class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        dic_n, dic_t = [], []

        for n in name:
            if len(dic_n) > 0 and n in dic_n[-1]:
                dic_n[-1][n] += 1
            else:
                dic_n.append({n: 1})
        
        for t in typed:
            if len(dic_t) > 0 and t in dic_t[-1]:
                dic_t[-1][t] += 1
            else:
                dic_t.append({t: 1})
        
        if len(dic_n) != len(dic_t):
            return False
        
        for i in range(len(dic_n)):
            key_n = list(dic_n[i].keys())[0]
            key_t = list(dic_t[i].keys())[0]

            if key_n != key_t or dic_n[i][key_n] > dic_t[i][key_t]:
                return False
        
        return True