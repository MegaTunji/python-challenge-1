# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

def order_list(item_name, price, quantity):

     order_list = [
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
]

order_dashes = '-' * 50
# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:



    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    print("-" * 50)
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i= i + 1 

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("What is the menu item number of the item you would like (q to quit): ")
            if menu_selection == "q":
                break

            # 3. Check if the customer typed a number
            elif menu_selection.isdigit():   
                menu_selection = int(menu_selection)

            else:
                print("Error, input is not a number.")


        # 4. Check if the menu selection is in the menu items
            if menu_selection in menu_items.keys():
                print("This item is in stock.")

            else:
            
                print(" This item is not part of our menu.")
                print("Please try another option.")

            # Store the item name as a variable
            item_name = menu_items[int(menu_selection)]

            print(f'You selected {item_name}')

             # Ask the customer for the quantity of the menu item
            quantity = input(f"{item_name}: If you would like more than one of these items, please specify the amount:")


             # Check if the quantity is a number, default to 1 if not
            if quantity.isdigit():
                quantity = int(quantity)
            else:
                quantity = 1

            print(order_dashes)
            print(f"You order,{quantity} of, {item_name}")

            # Order list

            order_list.append({
                "item_name": item_name,
                "price": value2,
                "Quantity": quantity
            })
            keep_ordering = True
            while keep_ordering:
            # Ask customer would they like to order more
                keep_ordering = bool(input("If you would like to keep ordering, Press 'y' or 'n' to stop."))

                     # Check customer's input
                match keep_ordering.lower():  
                    # Customer chose y
                    case 'y':
                     # Keep ordering
                     place_order = True
                     break
                    # Customer chose n
                    case 'n':
                    # Order Completed
                         place_order = False
                         print("Thank you for your order.")
                         break
                    # Invalid input response       
                    case _:
                    # Inform customer to try again
                        print("Please try again invalid input.")
  
  # create a for loop to loop through order list
  # design receipt 
        fixed_width = 30
        order_list = ['item_name', 'price', 'Quantity']
    for item_name, price, quantity in order_list:
        
        # Calculation of space needed
             num_spaces = fixed_width - len(item_name) -len(price) - len(quantity)

             formatted_receipt_line = item_name + '' * num_spaces + price + quantity

             print(formatted_receipt_line)