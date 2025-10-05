from pyscript import document, display

restaurant_name = "Bunny-Roo Bento" # String
owner_name = 'Meyer Cruz' # String
year_established = 2018 # Integer
has_delivery = True # Boolean
product_names = {"Onigiri (Rice Balls)", "Taiyaki", "Donburi Bowls", "Ramune", "Matcha Latte"} # List
business_hours = "24 HOURS" # String
menu_prices = {"Onigiri (Rice Balls)": 90.00,
    "Taiyaki": 100.00,
    "Donburi Bowls": 140.00,
    "Ramune": 120.00,
    "Matcha Latte": 160.00
}
common_allergens = ["Eggs", "Seafood", "Peanuts"] # List
tax_rate = 0.08 # Float

display(restaurant_name , target="restoname")
display(owner_name , target="ownername")
display(f"EST: {year_established}" , target="foundingyear")
