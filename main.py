import csv

class BudgetAnalysis:
    def __init__(self):
        self.dept_expenses = {}

    def get_dept_expenses(self):
        return self.dept_expenses

    def add_items(self, department, expense):
        exp = 0.0
        if expense:
            exp = float(expense)
        self.dept_expenses.setdefault(department, []).append(exp)

obj = BudgetAnalysis()

with open('city-of-seattle-2012-expenditures-dollars.csv', 'r') as file:
    i = 1
    reader = csv.reader(file, delimiter=',')
    for list in reader:
        if i != 1:
            obj.add_items(list[0], list[3])
        i+=1

for key, value in obj.get_dept_expenses().items():
    total_expenses = sum(value)
    currency = '${:,.2f}'.format(total_expenses)
    print(key.ljust(10) + " : " + currency)