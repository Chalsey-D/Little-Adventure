# Adventurer's starting inventory
consumables = ["potion"]
weapon = ["wooden sword"]
armor = []
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
  print("0.Go back")

  answer = int(input())

  #while answer == True:
#if you are buying a potion
    if answer == 1:
      for key,value in shop_consumables.items():
        print("Item: {} Price: {}g".format(key,value))
      purchase = input("\nPlease type which one do you want?")

      if purchase.lower() == "poiton" and wallet >= 25:
        consumables.append("poiton")
      elif purchase.lower() == "antidote" and wallet >= 50:
        consumables.append("antidote")
      else:
        print("You do not have enough money or I don't have what you want.")
  #if you are buying armor
    elif answer == 2:
      for key,value in shop_Armor.items():
        print ("Item: {} Price: {}g".format(key,value))
      purchase = input("\nPlease type which one do you want?")

      if purchase.lower() == "bronze helm" and wallet >= 75:
        armor.append("bronze helm")
      elif purchase.lower() == "chainmail" and wallet >= 300:
        armor.append("chainmail")
      elif purchase.lower() == "leather boots" and wallet >= 100:
        armor.append("leather boots")
      else:
        print("You do not have enough money or I don't have what you want.")
  #if you are buying weapons
    elif answer == 3:
      for key,value in shop_Weapons.items():
        print("Item: {} Price: {}g".format(key,value))
      purchase = input("\nPlease type which one do you want?")

      if purchase.lower() == "bronze sword" and wallet >= 150:
        weapon[0] = "bronze sword"
      elif purchase.lower() == "bow" and wallet >= 75:
        weapon.append("bow")
      elif purchase.lower() == "arrow" and wallet >= 100:
        weapon.append("arrow")
      else:
        print("You do not have enough money or I don't have what you want.")
    
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
  
  elif choice == 2:
    Go_to_Shop()
  
  #elif choice == 3:
    #Adventure()

  #elif choice == 4:
    #Go_Home()

  else:
    print("We are done here")

main()