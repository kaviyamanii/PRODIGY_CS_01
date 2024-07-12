#Task 01
#Caesar Chiper

def encrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave other characters unchanged
        else:
            result += char
            
    return result

def decrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        # Leave other characters unchanged
        else:
            result += char
            
    return result

def main():
    option = input("Choose one: \n1:'encrypt' to encrypt \n2:'decrypt' to decrypt\n ").lower()
    text = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if option == 'encrypt':
        encrypted_message = encrypt(text, shift)
        print("Encrypted message: " + encrypted_message)
    elif option == 'decrypt':
        decrypted_message = decrypt(text, shift)
        print("Decrypted message: " + decrypted_message)
    else:
        print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()