consumables = ["potion"]
weapon = ["wooden sword"]
armor = False

def main():
  #this is the menu the user will use.
  print("What would you like to do adventurer?\n")
  print("1.Check inventory")
  print("2.Go to Shop")
  print("3.Go on an Adventure")
  print("4.Go Home\n")

  choice = int(input())

  if choice == 1:
    print("Consumables = ",consumables)
    print("Weapon = ",weapon)
    print("Armor = ",armor)
  
  else:
    print("We are done here")

main()