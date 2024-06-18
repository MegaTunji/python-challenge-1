Menu dictionary
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
order_list = []



# Launch the store and present a greeting to the customer
print("Welcome to the Tunji's food truck, here to satisfy your appetite.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Get Customers Name
    customer_id = input("Enter your name or type 'no' to exit    ")
    if customer_id == 'no':
        break
    # Ask the customer from which menu category they want to order
    print(f"From which menu would you like to order {customer_id}? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

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
            menu_selection =input("What is the item number of the of your menu choice?")


            # 3. Check if the customer typed a number
            if menu_selection.isdigit():   
                menu_selection = int(menu_selection)

            else:
                print("Error, input is not a number.")


                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)


                # 4. Check if the menu selection is in the menu items
            if menu_selection in menu_items.keys():
                print("This item is in stock.")

            else:
                print(" This item is not part of our menu.")
                print("Please try another option.")
             # Store the item name as a variable
            
            item_name = menu_items[int(menu_selection)]['Item name']
            
            item_price = menu_items[int(menu_selection)]['Price']
            
            print(f'You selected {item_name} {item_price}')


                    
                    # Ask the customer for the quantity of the menu item
            quantity = input(f"{item_name}: If you would like more than one of these items, please specify the amount:") 



                    # Check if the quantity is a number, default to 1 if not
            if quantity.isdigit():
                        print(f'Okay, you ordered: {quantity}.')

            else:
                        quantity == 1
                        print(" INPUT error, so default quantity amount of 1 will be assigned to your order.")


            
                    # Add the item name, price, and quantity to the order list
            print(f'You ordered {quantity} of {item_name}')
            order_list.append({"Customer": customer_id,
                            "Item name": item_name,
                            "Price": item_price,
                             "Quantity": quantity})


    # 5. Check the customer's input
    keep_ordering = True
    while keep_ordering:
            # Ask customer would they like to order more
            keep_ordering = (input("If you would like to keep ordering, Press 'y' or 'n' to stop."))
            print('keep_ordering',keep_ordering.lower())
                     # Check customer's input
            match 1:
                case 1:
                      print("hey")
            match keep_ordering.lower():  
            # match 'y':
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


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Customer ID     Item name  | Price  | Quantity")
print("--------------------------|--------|----------")
print(order_list)

                        
# 6. Loop through the items in the customer's order
for order in order_list:
    print("this is")
    print(order)


            
    # 7. Store the dictionary items as variables
    customer_id = order['Customer']
    item_name = order['Item name'] 
    item_price = order["Price"]
    quantity = order['Quantity']
 
    
    # 8. Calculate the number of spaces for formatted printinG
    
    #customer_id_spaces = len("--------------------------") - len(customer_id)
    item_name_space = len("--------------------------") - len(item_name)
    item_price_space = len("--------") 
    quantity_space = len("----------") - len(quantity)


    


    # 9. Create space strings
    item_name_space_string = ' ' * item_name_space
    item_price_space_string = ' ' * item_price_space
    quantity_space_string = ' ' * quantity_space


    # 10. Print the item name, price, and quantity
    print(order)
    for order in order_list:
       print(f"{order['Item name']: <10} \
      {order['Price']:<10.2f} \
      {order['Quantity']:<10}")
# 11. Calculate the cost of the order using list comprehension
    order_list = [{"Quantity": 3, "item_price": 10},
              {"Quantity": 4, "item_price": 10}]

total_price = sum([order['Quantity'] * order['item_price'] for order in order_list])
print(f'You owe: {total_price}')
   
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

