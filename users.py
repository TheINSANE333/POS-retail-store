def create_user():

	username = input("Enter a username: ")

	with open("users.txt", "r") as f:
		for line in f:
			saved_name = line.strip().split("|")[0]
			if username == saved_name:
				print("Username already exists")
				return (-1)
	password = input("Enter a password: ")
	confirm_password = input("Confirm password: ")

	if password != confirm_password:
		print("Passwords do not match")
		return
	
	user_status = input("User status (Admin: 'A' | Normal User: 'N'):")
	
	with open("users.txt", "a") as f:
		f.write(username + "|" + password + "|" + user_status + "\n")


def remove_user():

	isDeleted = False

	with open("users.txt", "r") as f:
		lines = f.readlines()
		if (len(lines) == 1):
			print("Cannot remove last remaining user in database, maybe try creating more?")
			return

	username = input("Enter a username: ")

	with open("users.txt", "w") as f:
		for line in lines:
			line = line.strip()
			saved_name = line.split("|")[0]
			if saved_name != username:
				f.write(line)
			else:
				isDeleted = True
	
	if isDeleted:
		print("Removed user with name" + saved_name)
	else:
		print("Username does not exist")

def view_user():

	i = 0
	users = "Users: "

	with open("users.txt", "r") as f:
		lines = f.readlines()
		for line in lines:
			line = line.split("|")[0]
			users += line
			users += " "
		print(users)


def prompt_login():
	
	username = input("Enter your username: ")
	password = input("Enter your password: ")

	with open("users.txt", "r") as f:
		for line in f:
			line = line.strip()
			if line == "":
				continue
			line = line.split("|")
			saved_name = line[0]
			saved_pw = line[1]
			user_status = line[2]
			if ((username == saved_name) and (password == saved_pw)):
				print("Login Successful. Welcome back, " + saved_name)
				return (user_status);
			else:
				continue
		print("Login Failure")
		return (-1)
