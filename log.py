def view_log():
	
	n = 0
	lineCount = 0

	with open("log.log", "r") as f:
		lines = f.readlines()
	
	while True:
		try:
			line = lines[n]
			n += 1
			lineCount += 1
			print(line)
		except EOFError:
			break
	
