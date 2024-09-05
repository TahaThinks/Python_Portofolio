from converters import *

# Get Data from Client
client_input = input("Please Enter your message: ").upper()
moorse_code = ""

for character in client_input:
    if character in LETTERS:
        moorse_code += LETTERS[character] + '       '

print(moorse_code)