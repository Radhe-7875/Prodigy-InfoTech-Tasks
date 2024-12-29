def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    # Adjust the shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():  # Only process alphabetic characters
            # Determine if the character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    print("---------------------")
    
    # User input for mode
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return
    
    message = input("Enter the message: ").strip()
    
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Shift value must be an integer.")
        return
    
    result = caesar_cipher(message, shift, mode)
    
    print(f"Result ({mode}ed text): {result}")

if __name__ == "__main__":
    main()
