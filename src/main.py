import os

Loop = 0
Item1 = 0
Item2 = 0
Item3 = 0
Item4 = 0
Item5 = 0
Item6 = 0
Item7 = 0
Item8 = 0
Item9 = 0


print('Welcome to the Minecraft crafting calculator')
crafting_item = input('What are you crafting? ')
# print(crafting_item)
crafting_item_amount = int(input('How many are you crafting? '))
# print(crafting_item_amount)
crafting_needextra = input('List The Items you need ')
crafting_list = crafting_needextra.split()
# print(crafting_list)

file_name = 'crafting_requirements.txt'
mode = 'a' if os.path.exists(file_name) else 'w'



for i in crafting_list:
    if Loop == 0:
        Item1 = int(input('How many ' + crafting_list[0] + ' do you need? '))
    elif Loop == 1:
        Item2 = int(input('How many ' + crafting_list[1] + ' do you need? '))
    elif Loop == 2:
        Item3 = int(input('How many ' + crafting_list[2] + ' do you need? '))
    elif Loop == 3:
        Item4 = int(input('How many ' + crafting_list[3] + ' do you need? '))
    elif Loop == 4:
        Item5 = int(input('How many ' + crafting_list[4] + ' do you need? '))
    elif Loop == 5:
        Item6 = int(input('How many ' + crafting_list[5] + ' do you need? '))
    elif Loop == 6:
        Item7 = int(input('How many ' + crafting_list[6] + ' do you need? '))
    elif Loop == 7:
        Item8 = int(input('How many ' + crafting_list[7] + ' do you need? '))
    elif Loop == 8:
        Item9 = int(input('How many ' + crafting_list[8] + ' do you need? '))
    Loop += 1


Item1 = Item1 * crafting_item_amount
Item2 = Item2 * crafting_item_amount
Item3 = Item3 * crafting_item_amount
Item4 = Item4 * crafting_item_amount
Item5 = Item5 * crafting_item_amount
Item6 = Item6 * crafting_item_amount
Item7 = Item7 * crafting_item_amount
Item8 = Item8 * crafting_item_amount
Item9 = Item9 * crafting_item_amount


with open(file_name, mode) as file:
  file.write(f"Crafting item: {crafting_item}, Amount: {crafting_item_amount}\n")
  file.write("Items needed:\n")
  for index, item in enumerate(crafting_list):
      if index == 0:
          file.write(f"- {item}: {Item1} needed\n")
      elif index == 1:
          file.write(f"- {item}: {Item2} needed\n")
      elif index == 2:
          file.write(f"- {item}: {Item3} needed\n")
      elif index == 3:
          file.write(f"- {item}: {Item4} needed\n")
      elif index == 4:
          file.write(f"- {item}: {Item5} needed\n")
      elif index == 5:
          file.write(f"- {item}: {Item6} needed\n")
      elif index == 6:
          file.write(f"- {item}: {Item7} needed\n")
      elif index == 7:
          file.write(f"- {item}: {Item8} needed\n")
      elif index == 8:
          file.write(f"- {item}: {Item9} needed\n")
  file.write("\n")
