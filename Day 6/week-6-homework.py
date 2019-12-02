# Write a program to  decrypt files using the ROT13 algorithm
# more information about ROT 13 is here: https://en.wikipedia.org/wiki/ROT13


# use the function below to decrypt the sample.txt
# here is a function that decrypts characters by rotating them 13 places:
def decrypt(character):
    abc = "abcdefghijklmnopqrstuvwxyz"
    if abc.find(character) != -1:
        de = abc[(abc.find(character) + 13) % 26]
    else:
        de = character
    return de

# you will need to: open the file using open() read the whole file into a single string variable using read(), loop
# through the characters in the string variable calling the decrypt function for each character - append a result
# character by character print out the result

