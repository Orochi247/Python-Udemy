alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount # 7 -> 9
        shifted_position %= len(alphabet) # this will keep the index of the alphabets between 0-25, useful in cases of last letters which can return an index out of range error
        output_text += alphabet[shifted_position] #J
    
    print(f"Here in the {encode_or_decode}d result: {output_text}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)