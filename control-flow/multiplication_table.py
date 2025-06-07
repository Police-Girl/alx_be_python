tableNum = int(input("Enter a number to see its multiplication table:"))
tableSize = range (1,11)
#results = tableNum * tableSize
for x in tableSize:
	print(f"{tableNum} * {x} = {tableNum * x}")

