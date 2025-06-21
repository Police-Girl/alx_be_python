from shopping_list_manager import display_menu

def main():
        shopping_list = []
        while True:
                display_menu()
                choice = input("Enter your choice: ")
                if choice == '1':
                        add = input("Add an item: ")
                elif choice == '2':
                        remove = input("Remove an item: ")
                elif choice == '3':
                        print("Shopping List Manager")          #Questioning this ngl.
                elif choice == '4':
                        print(f"Goodbye")
                        break
                else:
                        print(f"Invalid choice. Please try again.")
if __name__ == "__main__":
	main()


