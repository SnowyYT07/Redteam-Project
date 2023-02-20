def caesar_cipher(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) + key - 65) % 26 + 65)
            else:
                encrypted += chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted += char
    return encrypted

message = input("Enter message to encrypt: ")
key = int(input("Enter key (number of positions to shift): "))
encrypted_message = caesar_cipher(message, key)
print("Encrypted message:", encrypted_message)
decrypted_message = caesar_cipher(encrypted_message, -key)
print("Decrypted message:", decrypted_message)