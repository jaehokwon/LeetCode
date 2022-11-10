"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = 0
        dic = {}
        
        for emp in employees:
            dic[emp.id] = emp
        
        queue = []
        queue.append(dic[id])
        
        while queue:
            emp = queue.pop(0)
            importance += emp.importance
            for sub in emp.subordinates:
                queue.append(dic[sub])
        
        return importance