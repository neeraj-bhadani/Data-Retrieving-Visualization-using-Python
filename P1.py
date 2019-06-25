alphabet='abcdefghijklmnopqrstuvwxyz0123456789'
newmsg = ''
key= 4

message= input('Enter the new message: ')

print('1. Encryption')
print('2. Decryption')

choice= input('Enter choice: ')

if choice=='1':
    for character in message:

        position= alphabet.find(character)
        newposition = (position + key)%36
        newchar=alphabet[newposition]
        print('Encrypted new character is: ', newchar)
        newmsg+=newchar
    print('Encrypted:', newmsg)

if choice=='2':
    for character in message:

        position= alphabet.find(character)
        newposition = (position - key)%36
        newchar=alphabet[newposition]
        print('Decrypted new character is: ', newchar)
        newmsg+=newchar
    print('Decrypted:', newmsg)
