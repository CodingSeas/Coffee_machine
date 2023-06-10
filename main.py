import time
from system_use import clear
from art import logo

# initial Resources
water = 300
coffee = 100
milk = 200
money = 0.0


# coffee types
def coffee_resource(ctype=None):
    """Return the amount of resource required for particular type of coffee and money earned."""
    if ctype == "espresso":
        water_c = 50
        coffee_c = 18
        milk_c = 0
        money_c = 1.5
    elif ctype == "latte":
        water_c = 200
        coffee_c = 24
        milk_c = 150
        money_c = 2.5
    elif ctype == "cappuccino":
        water_c = 250
        coffee_c = 24
        milk_c = 100
        money_c = 3
    else:
        water_c = 0
        coffee_c = 0
        milk_c = 0
        money_c = 0

    return water_c, coffee_c, milk_c, money_c


# Resources sufficient
def resource(ctype=None, water_u=water, coffee_u=coffee, milk_u=milk, money_u=money):
    """Returns the resource available."""
    if ctype == "RR":
        return f"Remaining Resource:\nWater: {water_u}ml\nMilk: {milk_u}ml\nCoffee: {coffee_u}g"
    elif ctype is None or ctype == "Report":
        pass
    else:
        water_r, coffee_r, milk_r, money_r = coffee_resource(ctype)
        water_u -= water_r
        coffee_u -= coffee_r
        milk_u -= milk_r
        money_u += money_r
    return water_u, coffee_u, milk_u, money_u


def transfer_money(quarters_t=0, dimes_t=0, nickels_t=0, pennies_t=0, ctype=None):
    money_paid = quarters_t * 0.25 + dimes_t * 0.1 + nickels_t * 0.05 + pennies_t * 0.01
    if coffee_resource(ctype)[3] == money_paid:
        return "Successful!", True
    elif coffee_resource(ctype)[3] < money_paid:
        return f"Successful!\nExtra money ${round(money_paid - coffee_resource(ctype)[3])} refunded.", True
    else:
        return f"Not enough ${coffee_resource(ctype)[3]} money required, ${money_paid} money refunded .", False


# print report
def report(ctype = None, water_e=water, coffee_e=coffee, milk_e=milk, money_e=money):
    """Gives detailed report."""
    water_r, coffee_r, milk_r, money_r = coffee_resource(ctype)
    if ctype != "report":
        result = f"""Cost of purchasing {ctype}:\nWater: {water_r}ml\nMilk: {milk_r}ml\nCoffee: {coffee_r}g
Money: ${money_r}\nEnjoy your {ctype}!"""
        return result
    else:
        water_r, coffee_r, milk_r, money_r = water_e, coffee_e, milk_e, money_e
        return f"Report:\nWater: {water_r}ml\nMilk: {milk_r}ml\nCoffee: {coffee_r}g\nMoney: ${money_r}"


def resource_check(resource_list_f=None, resource_req_list_f=None):
    """Checks if the list1 is greater than list2."""
    for i in range(0, len(resource_list_f) - 1):
        if resource_list_f[i]-resource_req_list_f[i] < 0:
            return False
    return True


while True:
    print(logo)

    # checking for resources
    print(resource("RR", water, coffee, milk, money))
    # What do you want
    coffee_type = input("What would you like? (espresso/latte/cappuccino)\n")
    money_reached = False
    if coffee_type == "off":
        break
    elif coffee_type != "report":
        # Checking for resources required.
        resource_list = resource(None, water, coffee, milk, money)
        resource_req_list = coffee_resource(coffee_type)

        if resource_check(resource_list, resource_req_list) and resource_req_list[3] > 0:
            # process coin
            print("Please insert Coins.")
            quarters = int(input("How many quarters? ") or 0)
            dimes = int(input("How many dimes? ") or 0)
            nickels = int(input("How many nickles? ") or 0)
            pennies = int(input("How many pennies? ") or 0)

            # check transaction successful?
            transaction = transfer_money(quarters, dimes, nickels, pennies, coffee_type)
            print(transaction[0], "\n")

            if transaction[1]:
                money_reached = True
                # Updating resources
                water, coffee, milk, money = resource(coffee_type, water, coffee, milk,  money)
        else:
            print("Sorry! Resource Depleted.")
    else:
        money_reached = True
    if money_reached:
        print(report(coffee_type, water, coffee, milk, money))
        print()
    else:
        print("Unsuccessful!")

    time.sleep(5)
    clear()
