"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import stock, personnel
from datetime import datetime, timedelta
from login_user import login, is_logged_in


# YOUR CODE STARTS HERE
current_time = datetime.now()
# Get the user name
user = input("Username: ")
# Greet the user
print(f"Halo and welcome {user}, to our site!")

# login


def login_terminal():
    print("do you want to login?\n"
      "1. Yes\n"
      "2. No")
    choise = int(input("Enter your choice here: "))

    if choise == 1:
        login()


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
# Show the menu and ask to pick a choice


def start():
    print("You can choose what you want to do here.\n"
          "1 List items warehouse\n"
          "2 Search an item and place an order\n"
          "3 Quit")
    choise = int(input("Put here the number what you like to do: "))
# If they pick 1

    if choise == 1:
        for state, items in warehouse1.items():
            for item in items:
                if "category" in item:
                    stock_date = datetime.strptime(item["date_of_stock"],
                        "%Y-%m-%d %H:%M:%S")
                    days_in_stock = (current_time - stock_date).days
                    print(f"Category: {item['category']}, State: {item['state']}, Date of Stock: {item['date_of_stock']}, Days in Stock: {days_in_stock} days")
        print(f"Total count of items in Warehouse 1 is: {len(items)}")

        for state, items in warehouse2.items():
            for item in items:
                if "category" in item:
                    stock_date = datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S")
                    days_in_stock = (current_time - stock_date).days
                    print(f"Category: {item['category']}, State: {item['state']}, Date of Stock:\n"
                      f"{item['date_of_stock']}, Days in Stock: {days_in_stock} days")
        print(f"Total count of items in Warehouse 2 is: {len(items)}")

        for state, items in warehouse3.items():
            for item in items:
                if "category" in item:
                    stock_date = datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S")
                    days_in_stock = (current_time - stock_date).days
                    print(f"Category: {item['category']}, State: {item['state']}, Date of Stock: {item['date_of_stock']}, Days in Stock: {days_in_stock} days")
        print(f"Total count of items in Warehouse 3 is: {len(items)}")

        for state, items in warehouse4.items():
            for item in items:
                if "category" in item:
                    stock_date = datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S")
                    days_in_stock = (current_time - stock_date).days
                    print(f"Category: {item['category']}, State: {item['state']}, Date of Stock: {item['date_of_stock']}, Days in Stock: {days_in_stock} days")
        print(f"Total count of items in Warehouse 4 is: {len(items)}")
        start()
# Else, if they pick 2

    elif choise == 2:
        print("In wich category are you looking for?:\n"
              "1 Search for a item\n"
              "2 Search a item in  warehouse1\n"
              "3 Search a item in  warehouse2\n"
              "4 Search a item in  warehouse3\n"
              "5 Search a item in  warehouse4\n"
              "6 Browsing by item state")
        search_choice = int(input("Put here the number what you like to do: "))
        if search_choice == 1:
            search = input("What are you looking for?: ")
            search_item(search)
        elif search_choice == 2:
            search = input("What are you looking for?: ")
            search_item_warehouse1(search)
        elif search_choice == 3:
            search = input("What are you looking for?: ")
            search_item_warehouse2(search)
        elif search_choice == 4:
            search = input("What are you looking for?: ")
            search_item_warehouse3(search)
        elif search_choice == 5:
            search = input("What are you looking for?: ")
            search_item_warehouse4(search)        
        elif search_choice == 6:
            search = input("In wich state are you looking for your item?:\n"
                           "We have:"
                           "Almost new\n"
                           "Funny\n"
                           "Elegant\n"
                           "High quality\n"
                           "Brand new\n"
                           "Wich state: ")
            item_search = input("Wich item are you looking for?: ")
            search_item_state(search, item_search)


# Else, if they pick 3
        elif choise == 3:
            bey()
# Else
        else:
            print("Invalid input")
            start()

# Search an item


def search_item(search):
    total_count = 0
    local = []

    for item in stock:
        if 'category' in item and search.lower() in item['category'].lower():
            if 'category' in item:
                total_count += 1
                local.append(item)
                stock_date = datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S")
                days_in_stock = (current_time - stock_date).days
                print(f"Item: {item['category']}, State: {item['state']}, Date of Stock:{days_in_stock} days")

    if total_count == 0:
        print("Not in stock")
    elif len(local) > 1:
        while True:
            print("Do you want to place an order?\n1 Yes\n2 No")
            buy = int(input("Put here the number what you like to do: "))
            if buy == 1:
                if is_logged_in():
                    shopping(total_count)
                else:
                    print("Please login first")
                    if login():
                        continue
                    else:
                        print("Login failed")

            elif buy == 2:
                bey()
            else:
                print("Invalid input you will go back to the previous")
                search_item(search)

    else:
        print(local[0])
# Search an item in warehouse 1


def search_item_warehouse1(search):
    total_count = 0
    local = []

    warehouse1 = {}

    for item in stock:
        warehouse = item.get("warehouse")
        if warehouse == 1:
            state = item.get("state")
            if state in warehouse1:
                warehouse1[state].append(item)
            else:
                warehouse1[state] = [item]

    for state, item in warehouse1.items():
        for item in item:
            if 'category' in item and search.lower() in item['category'].lower():
                if 'category' in item:
                    total_count += 1
                    local.append("Warehouse 1")

    if total_count == 0:
        print("Not in stock")
    elif len(local) >= 1:
        print("Do you want to place an order?\n1 Yes\n2 No\n3 Go back")
        choise_to_buy = int(input("Put here the number what you like to do: "))
        while True:
            if choise_to_buy == 1:
                if is_logged_in():
                    shopping(total_count)
                else:
                    print("Please login first")
                    if login():
                        continue
                    else:
                        print("Login failed")
            
            elif choise_to_buy == 2:
                bey()
            elif choise_to_buy == 3:
                print("You are going back to the start menu")
                start()

# Search an item in warehouse 2


def search_item_warehouse2(search):
    total_count = 0
    local = []

    for item in stock:
        warehouse = item.get("warehouse")
        if warehouse == 2:
            state = item.get("state")
            if state in warehouse2:
                warehouse2[state].append(item)
            else:
                warehouse2[state] = [item]

    for state, item in warehouse2.items():
        for item in item:
            if 'category' in item and search.lower() in item['category'].lower():
                if 'category' in item:
                    total_count += 1
                    local.append("Warehouse 2")

    if total_count == 0:
        print("Not in stock")
    elif len(local) >= 1:
        print("Do you want to place an order?\n1 Yes\n2 No\n3 Go back")
        choise_to_buy = int(input("Put here the number what you like to do: "))
        while True:
            if choise_to_buy == 1:
                if is_logged_in():
                    shopping(total_count)
                else:
                    print("Please login first")
                    if login():
                        continue
                    else:
                        print("Login failed")

            elif choise_to_buy == 2:
                bey()
            elif choise_to_buy == 3:
                print("You are going back to the start menu")
                start()

# Search an item in warehouse 3


def search_item_warehouse3(search):
    total_count = 0
    local = []

    for item in stock:
        warehouse = item.get("warehouse")
        if warehouse == 3:
            state = item.get("state")
            if state in warehouse3:
                warehouse3[state].append(item)
            else:
                warehouse3[state] = [item]

    for state, item in warehouse3.items():
        for item in item:
            if 'category' in item and search.lower() in item['category'].lower():
                if 'category' in item:
                    total_count += 1
                    local.append("Warehouse 3")

    if total_count == 0:
        print("Not in stock")
    elif len(local) >= 1:
        print("Do you want to place an order?\n1 Yes\n2 No\n3 Go back")
        choise_to_buy = int(input("Put here the number what you like to do: "))
        while True:
            if choise_to_buy == 1:
                if is_logged_in():
                    shopping(total_count)
                else:
                    print("Please login first")
                    if login():
                        continue
                    else:
                        print("Login failed")

            elif choise_to_buy == 2:
                bey()
            elif choise_to_buy == 3:
                print("You are going back to the start menu")
                start()

# Search an item in warehouse 4


def search_item_warehouse4(search):
    total_count = 0
    local = []

    for item in stock:
        warehouse = item.get("warehouse")
        if warehouse == 4:
            state = item.get("state")
            if state in warehouse4:
                warehouse4[state].append(item)
            else:
                warehouse4[state] = [item]

    for state, item in warehouse4.items():
        for item in item:
            if 'category' in item and search.lower() in item['category'].lower():
                if 'category' in item:
                    total_count += 1
                    local.append("Warehouse 4")

    if total_count == 0:
        print("Not in stock")
    elif len(local) >= 1:
        print("Do you want to place an order?\n1 Yes\n2 No\n3 Go back")
        choise_to_buy = int(input("Put here the number what you like to do: "))
        while True:
            if choise_to_buy == 1:
                if is_logged_in():
                    shopping(total_count)
                else:
                    print("Please login first")
                    if login():
                        continue
                    else:
                        print("Login failed")

            elif choise_to_buy == 2:
                bey()
            elif choise_to_buy == 3:
                print("You are going back to the start menu")
                start()

# Search an item in a state


def search_item_state(search, item_search):
    total_count = 0
    local = []

    for item in stock:
        if search.lower() in item["state"].lower() and item_search.lower() in item["category"].lower():
            local.append(item)
            total_count += 1

    if total_count == 0:
        print("Not in stock")
 
    elif total_count > 0:
        for item in local:
            stock_date = datetime.strptime(item["date_of_stock"],
                                                "%Y-%m-%d %H:%M:%S")
            days_in_stock = (current_time - stock_date).days
            print(f"Item: {item['category']}, State: {item['state']},"
                  "Date of Stock:{days_in_stock} days")
            print(f"Total count: {total_count}")
            print("Do you want to place an order?\n1 Yes\n2 No")
            buy = int(input("Put here the number what you like to do: "))
            while True:
                if buy == 1:
                    if is_logged_in():
                        shopping(total_count)
                    else:
                        print("Please login first")
                        if login():
                            continue
                        else:
                            print("Login failed")

                elif buy == 2:
                    bey()
                else:
                    print("Invalid input you will go back to the previous")
                    search_item(search)
    else:
        print("Not in stock")


# Place an order
def shopping(total_count):
    print(f"We have {total_count}, How many")
    quantity = int(input("Put here the number you like to buy: "))
    if quantity > 0 and quantity <= total_count:
        print(f"You bought {quantity} items. Thank you for your purchase!")
        print("Do you want to stay in our side?\n1 Yes\n2 No")
        buy = int(input("Put here the number what you like to do: "))
        if buy == 1:
            print("You go back to the start menu")
            start()
        elif buy == 2:
            bey()
        else:
            print("Invalid input you are going back to the start menu")
            start()
    else:
        print("We dont have that many items in stock")
        shopping(total_count)

# Bey User


def bey():
    print(f"Thank you for your visit and have a nice day {user}!")
    exit()

# Start menu


login_terminal()
start()
