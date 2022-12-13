# Program : Cashier Program

# User features 
# 1. Item addition / removal to basket
# 2. Print reciept
# 3. Discounts

# Admin features
# 1. Add / remove items
# 2. Add / remove discounts
# 3. View sales log


import os
import math
import items
import users
import log

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def print_options(usertype):
	if usertype == "A":
		print("-----ADMIN COMMANDS-----")
		print("additem : Add item")
		print("rmvitem : Remove item(s)")
		print("adduser : Add user")
		print("rmvuser : Remove user")
		print("viewuser: View users")
		print("viewlog : View sales log")
	elif usertype == "N":
		print("-----USER  COMMANDS-----")
	print("clear : Clear Screen")
	print("help : List Commands")
	print("exit : Exit Program")
	
	exec_cmd(usertype)

def exec_cmd(usertype):

	while True:
		error = 0
		cmdNotFound = False
		cmd = str(input("Enter a command: "))
		if usertype == "A":
			if cmd == "additem":
				error = items.add_item()
			elif cmd == "rmvitem":
				error = items.remove_item()
			elif cmd == "adduser":
				error = users.create_user()
			elif cmd == "rmvuser":
				error = users.remove_user()
			elif cmd == "viewuser":
				error = users.view_user()
			elif cmd == "viewlog":
				error = log.view_log()
				
		if cmd == "help":
			print_options(usertype)
		elif cmd == "clear":
			clear()
		elif cmd == "exit":
				exit()
		else:
			cmdNotFound = True

		if cmdNotFound and error == 0:
			print("Command not found. Type 'help' for a list of commands.")



def main():
	while True:
		usertype = users.prompt_login()
		if type(usertype) == str:
			break
	print_options(usertype)


if __name__ == "__main__":
	main()