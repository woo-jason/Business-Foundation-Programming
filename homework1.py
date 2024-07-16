alphabet_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alphabet_int_list = [i for i in range(0,26)]
right_shift = 12

# prints the list of letters to an array of integers
# print(alphabet_int_list)

encrpyted_messages_list=[]
for alphabet_index in range(len(alphabet_list)):
    encrpyted_index = (alphabet_index + right_shift) % len(alphabet_list)
    encrpyted_messages_list.append(alphabet_list[encrpyted_index])

# prints the shifted list of letters of the alphabet
# print(encrpyted_messages_list)

l = []
with open('encrypted_messages.txt', 'r') as encrypted_messages_file:
        encrypted_messages_filelist = encrypted_messages_file.readlines()
        l = [line.strip() for line in encrypted_messages_filelist]

# prints encrypted message
# print(l)

decrypted = []
for string in l:
    decrypted_string = ''
    for i in range(len(string)): 
        if string[i] != ' ':
            encrypted_index = (alphabet_list.index(string[i]) + right_shift) % len(alphabet_int_list)
            decrypted_string += alphabet_list[encrypted_index]
        else:
            decrypted_string += ' '
    decrypted_string += "\n"
    decrypted.append(decrypted_string)

with open('readme.txt', 'w') as f:
    f.writelines(decrypted)

