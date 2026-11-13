items = [
    {"name": "Pliers", "price": "$12.50", "in_stock": True},
    {"name": "Hammer", "price": "$25.00", "in_stock": False},
    {"name": "Screwdriver", "price": "$8.20", "in_stock": True},
]
def calculateAvailableTotal(items):
    startprice=0.0
    for item in items:
        if item['in_stock']:                          
            new_price = float(item['price'].replace('$', ''))
            print(f"Item: {item['name']} | Price: {new_price}")
            startprice = startprice + new_price
    print(f"Total cost: {startprice:.2f}")
    return sum                                 

calculateAvailableTotal(items)


