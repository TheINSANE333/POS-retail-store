items = {}

def import_items():

	with open("items.txt", "r") as f:
		for line in f:
			line = line.strip()
			if line == "":
				continue
			item = line.split("|")
			item_name = item[0]
			item_price = item[1]
			items[item_name] = item_price

def add_item():

	print("Add item")

	while True:
		item_name = str(input("Enter item name: "))
		if item_name == "":
			print("Item name cannot be empty")
			return (-1)
		break

	while True:
		try:
			item_price = float(input("Enter item price (RM): "))
		except ValueError:
			print("Item price must be a number")
			return (-1)
		break

	item_price = str(item_price)

	with open("items.txt", "a") as f:
		f.write(item_name + "|" + item_price + "\n")

def remove_item():
	
	count = 0
	
	print("Remove item(s)")

	while True:
		item_name = str(input("Enter item name: "))
		if item_name == "":
			print("Item name cannot be empty")
			continue
		break

	with open("items.txt", "r") as f:
		lines = f.readlines()

	with open("items.txt", "w") as f:
		for line in lines:
			saved_name = line.split("|")[0]
			if saved_name != item_name:
				f.write(line)
			else:
				count += 1

	if count == 0:
		print("Item not found")
		return (-1)
	else:
		print(str(count) + " item(s) removed")
	

