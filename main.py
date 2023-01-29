from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()
ok = True

while ok:

  order_name = input("Please input the name of the drink that you would like to order: (espresso/latte/cappuccino)")
  
  if order_name == "report":
    machine.report()
    money_machine.report()
    continue
    
  else:
    drink = menu.find_drink(order_name)
  
  
    if machine.is_resource_sufficient(drink):
  
      if money_machine.make_payment(drink.cost):
  
        machine.make_coffee(drink)
  if input("Would you like to order another drink? 'Y' or 'N':").upper() == 'Y':
    continue
  else:
    ok = False
      



