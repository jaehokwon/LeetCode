class ATM:

    def __init__(self):
        self.cash = [0] * 5
        self.values = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, val in enumerate(banknotesCount):
            self.cash[i] += val

    def withdraw(self, amount: int) -> List[int]:
        res = []
        for n, val in zip(self.cash[::-1], self.values[::-1]):
            need = min(n, amount // val)
            res = [need] + res
            amount -= need * val
        if amount == 0:
            self.deposit([-x for x in res])
            return res
        else:
            return [-1]