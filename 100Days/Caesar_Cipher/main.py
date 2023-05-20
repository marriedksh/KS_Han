import logo

print(logo.logo)
# Define the ceaser_disk
ceaser_disk = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def ceaser(txt, key, fw_rw):
    res = ""
    # For Encoding Condition
    if fw_rw == 'encode':
        # Loop through each character in the input 'txt'
        for i in txt:
            if i in ceaser_disk:
                # Get the position of the character in ceaser_disk and add the 'key'
                # % 37 --> To handle negative shift and IndexError
                pos = (ceaser_disk.index(i) + key) % 37
                # Get the corresponding character at the new position
                converted_txt = ceaser_disk[pos]
                # Update the result
                res += converted_txt
            else:
                # If the character is not in the ceaser_disk, append it as it is
                res += i
    # For Decoding condition
    elif fw_rw == 'decode':
        # Loop through each character in the input 'txt'
        for i in txt:
            if i in ceaser_disk:
                # Get the position of the character in ceaser_disk and add the 'key'
                # % 27 --> To handle negative shift and IndexError
                pos = (ceaser_disk.index(i) - key) % 37
                # Get the corresponding character at the new position
                converted_txt = ceaser_disk[pos]
                # Update the result for decoding
                res += converted_txt
            else:
                # If the character is not in the ceaser_disk, append it as it is
                res += i
    # Print the outcome.
    print(f"The {fw_rw}d text is '{res}'.")


should_con = True
# While loop as long as should_con is True
while should_con:
    # Ask user for the direction (Encode or Decode)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # validate the input if it's invalid
    while direction != 'encode' and direction != 'decode':
        direction = input("Wrong Input! Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # Ask the user for input text
    text = input("Type your message:\n").lower()
    # Ask the user for the shift number and error handling
    try:
        shift = int(input("Type the shift number:\n"))
        ceaser(text, shift, direction)
    except ValueError:
        print("Invalid Input. Please enter an integer for the shift number")
    # Ask the user if they want to continue
    result = input("Do u want to go again? Y/N \n").lower()

    if result == 'n':
        # End the loop if the user wants to stop
        should_con = False
        print("GoodBye")
