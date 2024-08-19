# problem to place highest valuable items in backpack

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value/weight

def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True) #sorts in place
    usedcapacity = 0
    totalvalue = 0
    for i in items:
        remainingcap = capacity - usedcapacity
        if remainingcap >= i.weight:
            usedcapacity = usedcapacity + i.weight
            totalvalue = totalvalue + i.value
        elif remainingcap > 0:
            usedcapacity = usedcapacity + remainingcap
            totalvalue = totalvalue + (remainingcap * i.ratio)
        else:
            break
    print(f"The total value is {totalvalue}")


item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)

custlist = [item1, item2, item3]
knapsackMethod(custlist, 50)
        
     