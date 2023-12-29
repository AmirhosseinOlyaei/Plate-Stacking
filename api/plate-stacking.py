# Plate Stacking Application

# Global list to store plates
plates = []


def add_plate():
    """
    Adds a plate to the top of the stack. Validates the plate size to ensure it is a positive integer
    and not larger than the plate below it. If the validation fails, it displays an error message.
    """
    print("\nAdd a plate\n===========")
    input_size = input("Enter a plate size: ")
    if not input_size.isdigit():
        print("Invalid input. Please enter a positive integer.")
        return

    size = int(input_size)
    if size <= 0:
        print("Plate size must be a positive integer.")
    elif not plates or plates[-1] >= size:
        plates.append(size)
        print("Success!")
    else:
        print(f"Cannot place a plate of size {
              size} on top of another plate of size {plates[-1]}.")


def print_plates():
    """
    Prints the current stack of plates. Plates are displayed in a stacked manner, with the largest
    plate at the bottom. If there are no plates, it displays a message indicating the stack is empty.
    """
    if not plates:
        print("There are no stacked plates.")
    else:
        print("\nPrint plates\n============")
        max_width = max(plates)  # Width of the largest plate
        for plate in reversed(plates):
            # Center each plate within the width of the largest plate
            print(("#" * plate).center(max_width))


def remove_plates():
    """
    Removes a specified number of plates from the top of the stack. Validates the number of plates
    to ensure it's a positive integer and not greater than the number of plates in the stack.
    Displays an error message if the validation fails.
    """
    if not plates:
        print("There are no plates to remove.")
        return

    print("\nRemove plates\n=============")
    print(f"Current stack: {', '.join(str(plate) for plate in plates)}")
    print(f"Number of plates: {len(plates)}")

    input_num = input("How many plates to remove?: ")
    if not input_num.isdigit():
        print("Invalid input. Please enter a positive integer.")
        return

    num = int(input_num)
    if num <= 0:
        print("Number of plates to remove must be a positive integer.")
    elif num > len(plates):
        print(f"Cannot remove more than {
              len(plates)} plates. You chose {num}.")
    else:
        for _ in range(num):
            plates.pop()
        print("Success!")


def main_menu():
    """
    Displays the main menu and handles user interaction. Users can choose to add a plate, print the
    stack of plates, remove plates, or exit the application. Invalid choices are handled gracefully.
    """
    while True:
        print("\nMenu\n================")
        print("0. [Exit]\n1. Add a plate\n2. Print plates\n3. Remove plates")
        choice = input("Select [0-3]: ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            add_plate()
        elif choice == "2":
            print_plates()
        elif choice == "3":
            remove_plates()
        else:
            print("Invalid choice. Please select from [0-3].")


# Run the application
if __name__ == "__main__":
    main_menu()
