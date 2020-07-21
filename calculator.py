from collections import Counter


class Calculator():
    """Class to calculate total price of every lead added to it"""

    def __init__(self, pricing_rules):
        """
        pricing_rules should follow this specific format -

        pricing_rules = [{'B': 10, 'R': 5, 'ST': 2.5}, {'bonus_chart':
        [{'item': 'B', 'quantity_more_than': 5, 'bonus_amount': 10, 'type': 'price'},
        {'item': 'R', 'quantity_more_than': 8, 'bonus_amount': 10, 'type': 'percentage'}]}]

        """
        self.pricing_rules = pricing_rules
        self.lead_list = []

    def add(self, lead_code):
        """Method to add new lead codes for the current class object"""
        self.lead_list.append(lead_code)
        return self.lead_list

    def total(self):
        """Method to calculate grand total for the lead codes"""
        total = 0
        lead_price_dict = self.pricing_rules[0]
        bonus = self.pricing_rules[-1]['bonus_chart']
        lead_dict = dict(Counter(self.lead_list))

        for item in lead_price_dict:
            if item in lead_dict:
                total += float(lead_price_dict[item])*float(lead_dict[item])

        for item in bonus:
            try:
                if lead_dict[item['item']] > item['quantity_more_than']:
                    if item['type'] == 'price':
                        total = total + float(item['bonus_amount'])
                    elif item['type'] == 'percentage':
                        total = total + (lead_dict[item['item']]*lead_price_dict[
                            item['item']] * float(item['bonus_amount'])//100)
            except KeyError:
                continue
        return total
