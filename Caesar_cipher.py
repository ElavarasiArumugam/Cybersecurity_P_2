def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine ASCII base (65 for uppercase, 97 for lowercase)
            start = ord('A') if char.isupper() else ord('a')
            
            # Mathematical transformation: (x - base + shift) % 26 + base
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            # Keep spaces and punctuation unchanged
            result += char
    return result

# --- Execution ---
user_input = input("Enter text to encrypt: ")
key = int(input("Enter shift key (integer): "))

# Encryption
encrypted = caesar_cipher(user_input, key, mode='encrypt')
print(f"Encrypted: {encrypted}")

# Decryption
decrypted = caesar_cipher(encrypted, key, mode='decrypt')
print(f"Decrypted: {decrypted}")