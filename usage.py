from calculator import Calculator


pricing_rules = [{'B': 10, 'R': 5, 'ST': 2.5}, {'bonus_chart':
                                                [{'item': 'B', 'quantity_more_than': 5, 'bonus_amount': 10, 'type': 'price'},
                                                 {'item': 'R', 'quantity_more_than': 8, 'bonus_amount': 10, 'type': 'percentage'}]}]


calculator = Calculator(pricing_rules)
calculator.add('B')
calculator.add('R')
calculator.add('R')
calculator.add('R')
calculator.add('R')
calculator.add('R')
calculator.add('R')
calculator.add('R')
calculator.add('R')
calculator.add('R')
calculator.add('R')


total = calculator.total()
print(total)
