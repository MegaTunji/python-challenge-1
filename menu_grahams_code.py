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
order_lists = []


def order_list(item_name, price, quantity):
    add_order(order_list):
    order_list.appended(order_list)

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


# Launch the store and present a greeting to the customer
    print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:

            # 2. Ask customer to input menu item number

            menu_selection = input("What is the menu item number of the item you would like (q to quit): ")
            if menu_selection == "q":
                break
            # 3. Check if the customer typed a number
            if menu_selection.isdigit():   
                menu_selection = int(menu_selection)

            else:
                print("Error, input is not a number.")

             # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():
                    selected_item = (menu[menu_selection])
                    selected_item = menu.index(menu_selection)
                
                    print("This item is in stock.")

                else:
                     print(" This item is not part of our menu.")
                     print("Please try another option.")
    

                quantity = input(f"{selected_item}: If you would like more than one of these items please specify the amount.")

                if quantity.isdigit():
                        quantity = int(quantity)
                        print(f"{quantity} is the amount that will be added to your order.")

        
else:
           quantity == 1   
           print("Default quantity of one will be added to you order.")
           
             
           
           while True:
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
# Once order is complete
print('-' * 45)
print("Your Order Review:")



                

# 6. Loop through the items in the customer's order
for key, value in menu[menu_selection].items():
     for order_list in order_lists:
                     print(f"Item name:{menu[selected_item]}")
                     print()
 
            # 7. Store the dictionary items as variables
                menu_category_name = menu_items[int(menu_category)]


            # 8. Calculate the number of spaces for formatted printing
            num_item_spaces = 24 - len(key + key2) - 3
            item_spaces = " " * num_item_spaces
            print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
            menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
             # 9. Create space strings

             # 10. Print the item name, price, and quantity
            print(order_list)
            
             # 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices. 
sum(price * quantity)
 