alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

key = "yes"
print("\n\n******************  Welcome To The Encoder & Decoder  *************************")
while key == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    while shift >= 27:
        shift //= 26


    # TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

    # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
    #  by the shift amount and print the encrypted text.

    # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

    # TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
    #  message.

    def encode(text, shift):
        text = list(text)
        for i in range(0, len(text)):
            for j in range(0, 26):

                if text[i] == alphabet[j]:
                    if j + shift > 25:
                        text[i] = alphabet[shift-(26-j)]
                    else:
                        text[i] = alphabet[j + shift]
                    break
        return text


    def decode(text, shift):
        text = list(text)
        for i in range(0, len(text)):
            for j in range(0, 26):
                if text[i] == alphabet[j]:
                    if j-shift < 0:
                        text[i] = alphabet[26-(shift-j)]

                    else:
                       text[i] = alphabet[j - shift]
                    break

        return text


    if direction == "encode":
        print("".join(encode(text, shift)))

    elif direction == "decode":
        print("".join(decode(text, shift)))
    key = str(input("Type 'yes' to start or 'no' to stop:- "))




print("\n*************** Thank You !! ***************\n*************** GoodBye ***************")
