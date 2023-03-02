import random

def roll_dice (sides):
  sides = random.randint(1, sides)
  return sides

def roll_dice_6_and_8 ():
  roll_6_sides = roll_dice(6)
  roll_8_sides = roll_dice(8)
  character_health = roll_6_sides * roll_8_sides
  return character_health

print("🥷🏾 Character Health Stats 🥷🏾")

character = input("Do you have a charcacter?  ")

while character == "yes":
  character_name = input("Character Name:  ")
  character_health = str(roll_dice_6_and_8 ())
  print("The character", character_name, "has", character_health, "left")
  character = input("Do you have another character?  ")