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


# From menu dictionary  Meals select Burger
print(menu["Meals"]['Burger'])

# Print all the pizza type
print(menu['Meals']['Pizza'])

# Price for Cheese Pizza
print(menu['Meals']["Pizza"]['Cheese'])


# Print Drink options
print

# Large Soda types
print(menu["Drinks"]["Soda"]['Large'])

# The price of rice pudding
print(menu['Dessert']["Rice pudding"])


# 1 Green tea and cheesecake
print(menu["Drinks"]['Tea']["Green"])
print(menu["Dessert"]['Cheesecake'])

drink = (menu["Drinks"]['Tea']['Green'])
food = (menu["Dessert"]['Cheesecake'])

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
        i= i + 1 
print(menu_items)