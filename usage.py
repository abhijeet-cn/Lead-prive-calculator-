from calculator import Calculator


pricing_rules = [{'B': 10, 'R': 5, 'ST': 2.5}, {'bonus_chart':
                                                [{'item': 'B', 'quantity_more_than': 5, 'bonus_amount': 10, 'type': 'price'},
                                                 {'item': 'R', 'quantity_more_than': 8, 'bonus_amount': 10, 'type': 'percentage'}]}]


# Test case 1
calculator = Calculator(pricing_rules)
calculator.add('B')
calculator.add('B')
calculator.add('B')
calculator.add('B')
calculator.add('B')
calculator.add('B')
calculator.add('R')
calculator.add('R')
calculator.add('ST')
total = calculator.total()
print(total)

# Test case 2
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


# Test case 3
calculator = Calculator(pricing_rules)
calculator.add('B')
calculator.add('R')
calculator.add('ST')
calculator.add('ST')
calculator.add('R')
calculator.add('R')
calculator.add('R')
calculator.add('R')
total = calculator.total()
print(total)

# Test case 4
calculator = Calculator(pricing_rules)
calculator.add('B')
calculator.add('B')
calculator.add('B')
calculator.add('R')
calculator.add('ST')
calculator.add('ST')
calculator.add('R')
calculator.add('R')
total = calculator.total()
print(total)


pricing_rules = [{'B': 10, 'R': 5, 'ST': 2.5}, {'bonus_chart':
                                                [{'item': 'R', 'quantity_more_than': 2, 'bonus_amount': 100, 'type': 'percentage'}]}]


# Test case 5
calculator = Calculator(pricing_rules)
calculator.add('R')
calculator.add('R')
calculator.add('R')
total = calculator.total()
print(total)


# Test case 5
calculator = Calculator(pricing_rules)
calculator.add('B')
calculator.add('B')
calculator.add('B')
calculator.add('R')
calculator.add('R')
calculator.add('R')
calculator.add('R')
calculator.add('R')
calculator.add('ST')
total = calculator.total()
print(total)
