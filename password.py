import random
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = [i.upper() for i in lower_letters]
symbols = ["'", "#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","]"]
allchars = lower_letters.copy() + upper_letters.copy() + symbols.copy()

def password():
    num_of_chars = int(input('Number of characters: '))
    pswd = ''
    for i in range(num_of_chars):
        pswd += random.choice(allchars)
    print(pswd)
    print('')

def newpswd():
    again = input('New Password? (Y/N): ').lower()
    while again == 'y':
        password()
        print('')
        newpswd()
    else:
        exit()


password()
newpswd()




