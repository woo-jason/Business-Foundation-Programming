import sys 

# create a list of characters of the alphabet
alphabet_list = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+={}[]\|:;\'"<>,./?`~')

#create cipher alphabet through loop
def get_cipher_alphabet(shift):
    my_list=[]
    for i in range(len(alphabet_list)):
        shifted_index = (i + shift) % len(alphabet_list)
        my_list.append(alphabet_list[shifted_index])
    return my_list

# open the file of encrypted messages in read mode, call it encrypted_messages_file
with open('encrypted_messages.txt', 'r') as encrypted_messages_file:
    # readlines() reads all the lines of a file in one go and returns each line as a string element in a list
    encrypted_messages_list = encrypted_messages_file.readlines()

    # we use list compression to, for each line in the list, remove the whitespace (i.e. the new line character)
    # and then store the results in a list
    encrypted_messages_list = [line.strip() for line in encrypted_messages_list]
'''
This is a placeholder function. It should behave like:
shift_value = get_key('PICK UP THAT CAN CITIZEN',':X TUQ7k & 97QY3 4V 8%2R418klmnopqrst')
i.e. shift_value == 15
'''
def get_key(plaintext_message,cipher_message):
    # TODO
    a = alphabet_list.index(plaintext_message[0]) # find index of 'P' in alphabet
    b = alphabet_list.index(cipher_message[0]) # find index of ':' in alphabet
    key = b - a
    return key


# in command line:
# python3 hw1_solution.py encoded_messages.txt "pick up that can citizen"
# sys.argv = [sys.argv[0]      sys.arg[1]       sys.argv[2] ]

# given a list of strings, an original alphabet, and a cipher alphabet, 
# return a list of strings where each character has been appropriately shifted
def get_shifted_strings(list_of_strings,orig_alphabet,cipher_alphabet):
    #create new list of the decrypted messages
    new_string_list = []
    for message in encrypted_messages_list:
        new_string = ''
        for character in message:
            if character == " ":
                new_string = new_string + character
            else:
                letter_index = cipher_alphabet.index(character)
                new_string = new_string + orig_alphabet[letter_index]
        new_string_list.append(new_string)
    return new_string_list


if not len(sys.argv)==3:
    print('This program expects either a file name and a shift value, or a file name and a string as input')
    exit()

# if encrypting, sys.argv[1] should be a file name and sys.argv[2] should be a shift value
# if decrypting, sys.argv[1] should be a file name and sys.argv[2] should be a string
# we can tell based on sys.argv[2] if the user wanted to encode or decode
encode=True
try:
    file_name = sys.argv[1]
    shift_value = int(sys.argv[2])
    print('you want to encrypt '+file_name+' using a shift value of '+str(shift_value))
except:
    encode=False
    file_name = sys.argv[1]
    plain_text = sys.argv[2]
    print('you want to decrypt an encrypted file ('+ file_name +') and you know that the decoded message is '+ plain_text)

# open the file of messages in read mode, call it messages_file
with open(file_name, 'r') as messages_file:
    # readlines() reads all the lines of a file in one go and returns each line as a string element in a list
    messages_list = messages_file.readlines()

    # we use list compression to, for each line in the list, remove the whitespace (i.e. the new line character)
    # and then store the results in a list
    messages_list = [line.strip() for line in messages_list]


# shift_value = get_key(messages_list[0],plain_text)

if not encode:
    key = get_key(messages_list[0], plain_text)
    cipher_alphabet_shifted = get_cipher_alphabet(key)
    message_list = get_shifted_strings(messages_list, alphabet_list, cipher_alphabet_shifted)
if encode: 
    key = int(sys.argv[2])
    cipher_alphabet_shifted = get_cipher_alphabet(key)
    message_list = get_shifted_strings(messages_list, cipher_alphabet_shifted, alphabet_list)

#write the decrypted list into a text file
with open('result.txt', 'w') as new_text_file:
    for message in message_list:
        new_text_file.write(message + "\n")

print("Decrpyted messages successfully written to text file")