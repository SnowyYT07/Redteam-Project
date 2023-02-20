def rot13(text):
    """Encode/decode text using ROT13 cipher"""
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            result += char
    return result

plaintext = input("Enter the text to encode:")
ciphertext = rot13(plaintext)
print("Text encoded:",ciphertext)  
decoded_plaintext = rot13(ciphertext)
print("Text Decoded",decoded_plaintext)