print("Welcome to the Food Menu Program!")
print("select the option from below:")
print("1. Show food list")
print("2. Add food")
print("3. Remove food")
print("4. Count items")
print("5. Exit")

food_list = ["Pizza", "Burger", "Pasta", "Salad"]

while True:
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        print("Food List:", food_list)
    elif choice == "2":
        new_food = input("Enter the food item to add: ")
        food_list.append(new_food)
        print(f"{new_food} has been added to the food list.")
    elif choice == "3":
        food_to_remove = input("Enter the food item to remove: ")
        if food_to_remove in food_list:
            food_list.remove(food_to_remove)
            print(f"{food_to_remove} has been removed from the food list.")
        else:
            print(f"{food_to_remove} is not in the food list.")
    elif choice == "4":
        print(len(food_list))
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice")
    
      