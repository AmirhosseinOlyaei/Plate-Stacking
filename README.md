# Plate Stacking Program

This Python program simulates a plate stacking system, allowing users to add plates, print the current stack, and remove plates from the top of the stack.

## High-Level Requirements

### Add a Plate

- Add a plate to the top of the stack.
- Plates are represented by positive integers.
- Do not add plates with a size less than or equal to zero.
- Check if the plate below is greater than or equal to the current plate size.
- Display success or error messages accordingly.

### Print Plates

- Display the stack of plates in the terminal.
- Plates should stack vertically, with the largest plate on the bottom and the smallest on the top.
- Display a message if there are no plates.

### Remove Plates

- Remove a given number of plates from the top of the stack.
- The number of plates to remove must be a positive integer.
- Reject the operation and issue a warning if the input is less than or equal to zero.
- Reject the operation and issue a warning if there are too many plates selected.
- Display success or error messages accordingly.

## Technical Requirements

- Use a Python list to track plates at the file scope.
- Each menu item should be a function.
- Additional utility functions can be added as needed.

## Usage

1. Run the program.
2. Follow the on-screen menu to add plates, print the stack, or remove plates.
3. Enter plate sizes or the number of plates to remove when prompted.

## Example

### Add a Plate

```
Add a plate
===========
Enter a plate size: 10
Success!
```

### Print Plates

```
Print plates
============
    ###
  ######
 ########
##########
```

### Remove Plates

```
Remove plates
=============
How many plates to remove?: 2
Success!
```

### Add a Plate

- [ ] The application provides the user with an option to add a plate to the top of the stack.
- [ ] The user is prompted to enter a plate size.
- [ ] The application validates the plate size.
- [ ] Plate sizes must be positive integers.
- [ ] Plate sizes must be less than or equal to the size of the plate below it.
- [ ] If the plate size is invalid, the application displays an error message and does not add the plate to the stack.
- [ ] If the plate size is valid, the application adds the plate to the stack and displays a success message.

### Print Plates

- [ ] The application provides the user with an option to print the plates.
- [ ] The application prints the plates to the terminal.
- [ ] Plates stack vertically, with the largest plate on the bottom and the smallest plate on the top.
- [ ] If there are no plates, the application displays a message.

### Remove Plates

- [ ] The application provides the user with an option to remove plates from the top of the stack.
- [ ] If there are no plates on the stack, the application displays a message.
- [ ] If there are plates on the stack, the user is prompted to enter the number of plates to remove.
- [ ] The application validates the number of plates to remove.
- [ ] The number of plates to remove must be a positive integer.
- [ ] The number of plates to remove must be less than or equal to the number of plates on the stack.
- [ ] If the number of plates to remove is invalid, the application displays an error message and does not remove any plates.
- [ ] If the number of plates to remove is valid, the application removes the plates from the stack and displays a success message.

### Technical Requirements

- [ ] The application uses a Python list (defined at file scope) to track plates.
- [ ] The bottom plate is the first index.
- [ ] A plate is represented by a positive integer, which is also the plate's size.
- [ ] The application uses the int function to convert user input to an integer.
- [ ] Python code is idiomatic.
- [ ] The application uses functions to organize code.

### Complete and Continue

- [ ] Submission process completed.

## Acknowledgments

Special thanks and a shout out to the following individuals and organizations:

- [Dev10](https://www.dev-10.com/)

## Contact

If you have any questions or feedback, feel free to reach out to [Amir](https://www.linkedin.com/in/amirhossein-olyaei/).

## License

This project is licensed under the MIT License.
