def encode(text, k):
    encoded_text = ''
    for char in text:
        if char.isalpha():
            ascii_val = ord(char) - k
            encoded_text += chr(ascii_val)
    return encoded_text

def decode(text, n):
    decoded_text = ''
    for char in text: 
        if char.isalpha():
            ascii_val = ord(char) + k
            decoded_text += chr(ascii_val)
    return decoded_text
   

choice = input("Enter 1 to decode or 2 to encode: ")

if choice == '1':
    text = input("Enter the string to decode: ")
    k = int(input("Enter the shift value (k): "))
    decoded_text = decode(text, k)
    print("Decoded text:", decoded_text)
elif choice == '2':
    text = input("Enter the string to encode: ")
    k = int(input("Enter the shift value (k): "))
    encoded_text = encode(text, k)
    print("Encoded text:", encoded_text)
else:
    print("Invalid choice. Please enter 1 or 2.")