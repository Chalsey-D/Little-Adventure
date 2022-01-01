# Adventurer's starting inventory
consumables = ["potion"]
weapon = ["wooden sword"]
armor = False
wallet = 0

#Shop's starting inventory
shop_consumables = {
  "poiton": 25,
  "antidote":50,
}
shop_Armor = {
  "bronze helm":75,
  "chainmail":300,
  "leather boots":100
}

shop_Weapons = {
  "bronze sword":150,
  "bow":75,
  "arrow":100
}

#this function checks the inventory
def Check_inventory():
  print("Consumables = ",consumables)
  print("Weapon = ",weapon)
  print("Armor = ",armor)
  print("Money = ",wallet)

#this function creates the shop
def Go_to_Shop():
  print("Hello what are you buying?\n")
  print("1.Consumables")
  print("2.Armor")
  print("3.Weapons")

  answer = int(input())

#if you are buying a potion
  if answer == 1:
    for key,value in shop_consumables.items():
      print("Item: {} Price: {}g".format(key,value))
    purchase = input("\nWhich do you want?")

    if purchase.lower() == "poiton" and wallet >= 25:
      consumables.append("poiton")
    elif purchase.lower() == "antidote" and wallet >= 50:
      consumables.append("antidote")
    else:
      print("You do not have enough money or I don't have what you want.")
#if you are buying an antidote
  #elif answer == 2:

    
#def Adventure():

#def Go_Home():

#this is the menu
def main():
  #this is the menu the user will use.
  print("What would you like to do adventurer?\n")
  print("1.Check inventory")
  print("2.Go to Shop")
  print("3.Go on an Adventure")
  print("4.Go Home\n")

  choice = int(input())

  if choice == 1:
    Check_inventory()
  
  elif == 2:
    Go_to_Shop()
  
  #elif == 3:
    #Adventure()

  #elif == 4:
    #Go_Home()

  else:
    print("We are done here")

main()