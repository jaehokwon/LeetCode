class ATM:

    def __init__(self):
        self.dollors = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.dollors[i] += banknotesCount[i]
        
        print(self.dollors)

    def withdraw(self, amount: int) -> List[int]:
        res = [0, 0, 0, 0, 0]

        for i in range(len(self.dollors) - 1, -1, -1):
            if amount > 0:
                cnt, tot = self.availableWithdraw(amount, i)
                if cnt > 0:
                    res[i] = cnt
                    amount -= tot
        
        if amount == 0:
            for i in range(len(self.dollors)):
                self.dollors[i] -= res[i]

        print(res if amount == 0 else [-1])

        return res if amount == 0 else [-1]
    
    def availableWithdraw(self, amount: int, denominations: int) -> Tuple[int, int]:
        convert_dollor = 0

        if denominations == 0:
            convert_dollor = 20
        elif denominations == 1:
            convert_dollor = 50
        elif denominations == 2:
            convert_dollor = 100
        elif denominations == 3:
            convert_dollor = 200
        else:
            convert_dollor = 500
        
        cnt = amount // convert_dollor

        if self.dollors[denominations] < cnt:
            cnt = self.dollors[denominations]
        
        return cnt, cnt * convert_dollor