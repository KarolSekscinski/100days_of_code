
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}


def check_resources(user_ordered):
    resources_needed = MENU[user_ordered]['ingredients']
    if resources_needed['water'] > resources['water']:
        print("Sorry there is not enough water")
        return False
    elif not user_ordered == 'espresso' and resources_needed['milk'] > resources['milk']:
        print("Sorry there is not enough milk")
        return False
    elif resources_needed['coffee'] > resources['coffee']:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


def coins_operator(user_ordered):
    money_needed = MENU[user_ordered]['cost']
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money_inserted = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    change = round(money_inserted - money_needed, 2)
    if change < 0:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        print(f"Here is ${change} in change")
        return True


should_be_working = True
money = 0
while should_be_working:

    user_order = input("What would you like? (espresso/latte/cappuccino):")

    if user_order == "off":
        should_be_working = False
    elif user_order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif user_order == "refill":
        resources['water'] += int(input("How much water do you refill?: "))
        resources['milk'] += int(input("How much milk do you refill?: "))
        resources['coffee'] += int(input("How much coffee do you refill?: "))
        print(f"Here is your profit: ${money}")
        money = 0

    elif user_order == 'espresso' or user_order == 'latte' or user_order == 'cappuccino':
        if check_resources(user_ordered=user_order):

            if coins_operator(user_ordered=user_order):
                resources_needed = MENU[user_order]['ingredients']

                for key in resources_needed:
                    resources[key] -= resources_needed[key]
                money += MENU[user_order]['cost']
                print(f"Here is your {user_order}. Enjoy ☕☕☕")
    else:
        print("Please choose your coffee from ESPRESSO, LATTE, CAPPUCCINO. Check for typos")



