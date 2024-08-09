def caesar_cipher(text, shift, mode):  
    result = ""  
    
    # Adjust shift for decryption  
    if mode == "decrypt":  
        shift = -shift  
    
    for char in text:  
        if char.isalpha():  # Check if character is a letter  
            shift_base = 65 if char.isupper() else 97  # Base for uppercase or lowercase  
            # Perform the shift and wrap around using modulo  
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)  
        else:  
            result += char  # Non-alphabetic characters remain unchanged  
    
    return result  

# User input  
message = input("Enter the message: ")  
shift_value = int(input("Enter the shift value: "))  
action = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()  

if action in ["encrypt", "decrypt"]:  
    result = caesar_cipher(message, shift_value, action)  
    print(f"Result: {result}")  
else:  
    print("Invalid action! Please type 'encrypt' or 'decrypt'.")  
