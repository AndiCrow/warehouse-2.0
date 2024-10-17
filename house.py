'''
All warehouses
'''
from data import stock
from datetime import datetime
current_time = datetime.now()

warehouse1 = {}
warehouse2 = {}
warehouse3 = {}
warehouse4 = {}

for item in stock:
    warehouse = item.get("warehouse")
    if warehouse == 1:
        state = item.get("state")
        if state in warehouse1:
            warehouse1[state].append(item)
        else:
            warehouse1[state] = [item]
    elif warehouse == 2:
        state = item.get("state")
        if state in warehouse2:
            warehouse2[state].append(item)
        else:
            warehouse2[state] = [item]
    elif warehouse == 3:
        state = item.get("state")
        if state in warehouse3:
            warehouse3[state].append(item)
        else:
            warehouse3[state] = [item]
    elif warehouse == 4:
        state = item.get("state")
        if state in warehouse4:
            warehouse4[state].append(item)
        else:
            warehouse4[state] = [item]


def warehouse1():
    for state, items in warehouse1.items():
        for item in items:
            if "category" in item:
                    stock_date = datetime.strptime(item["date_of_stock"],
                        "%Y-%m-%d %H:%M:%S")
                    days_in_stock = (current_time - stock_date).days
                    print(f"Category: {item['category']}, State: {item['state']}, Date of Stock: {item['date_of_stock']}, Days in Stock: {days_in_stock} days")
        print(f"Total count of items in Warehouse 1 is: {len(items)}")


def warehouse2():
    for state, items in warehouse2.items():
        for item in items:
            if "category" in item:
                stock_date = datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S")
                days_in_stock = (current_time - stock_date).days
                print(f"Category: {item['category']}, State: {item['state']}, Date of Stock:\n"
                      f"{item['date_of_stock']}, Days in Stock: {days_in_stock} days")
            print(f"Total count of items in Warehouse 2 is: {len(items)}")
     

def warehouse3():
    for state, items in warehouse3.items():
            for item in items:
                if "category" in item:
                    stock_date = datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S")
                    days_in_stock = (current_time - stock_date).days
                    print(f"Category: {item['category']}, State: {item['state']}, Date of Stock: {item['date_of_stock']}, Days in Stock: {days_in_stock} days")
            print(f"Total count of items in Warehouse 3 is: {len(items)}")


def warehouse4():
    for state, items in warehouse4.items():
            for item in items:
                if "category" in item:
                    stock_date = datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S")
                    days_in_stock = (current_time - stock_date).days
                    print(f"Category: {item['category']}, State: {item['state']}, Date of Stock: {item['date_of_stock']}, Days in Stock: {days_in_stock} days")
            print(f"Total count of items in Warehouse 4 is: {len(items)}")


if __name__ == "__main__":
    warehouse1()
    warehouse2()
    warehouse3()
    warehouse4()
