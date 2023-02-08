class Solution:
    def maximum69Number(self, num: int) -> int:
        numText = list(str(num))
        lenText = len(numText)
        indexSix = -1
        for i in range(lenText):
            if indexSix == -1 and numText[i] == '6':
                indexSix = i
                break
        if indexSix == -1:
            return num
        else:
            numText[indexSix] = '9'
            return int(''.join(numText))