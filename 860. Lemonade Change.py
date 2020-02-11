'''
easy

At a lemonade stand, each lemonade costs $5. 

Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {"5":0, "10":0}
        for value in bills:
            if value == 5: d["5"] += 1
            elif value == 10: 
                if d["5"] >= 1: d["5"] -= 1;d["10"] += 1
                else: return False
            else: 
                if d["10"] >= 1 and d["5"] >= 1: d["10"] -= 1; d["5"] -= 1
                elif d["10"]==0 and d["5"] >= 3: d["5"] -= 3
                else: return False
        return True


