def display_menu():
	print("Shopping List Manager")
	print("1. Add Item")
	print("2. Remove Item")
	print("3. View List")
	print("4. Exit")

def main():
	shopping_list = []
	while true:
		display_menu()
		choice = input("Enter the item to add: ")
		if choice == '1':
			add = input("Add an item: ")
		elif choice == '2':
			remove = input("Remove an item: ")
		elif choice == '3':
			print("Shopping List Manager")  	#Questioning this ngl.
		elif choice == '4':
			print(f"Goodbye")
			break
		else:
			print(f"Invalid choice. Please try again.")
if __name__ == "__main__":
	main()
