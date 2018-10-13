alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
stringToDecrypt = input("Please enter a message to decrypt: ")
stringToDecrypt = stringToDecrypt.upper()
shiftAmount = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25]
for decryptShift in shiftAmount:
    decryptedString = ""
    for currentCharacter in stringToDecrypt:
        position = alphabet.find(currentCharacter)
        newPosition = position + decryptShift
        if currentCharacter in alphabet:
            decryptedString = decryptedString + alphabet[newPosition]
        else:
            decryptedString = decryptedString + currentCharacter
    print("Your decrypted message is", decryptedString)