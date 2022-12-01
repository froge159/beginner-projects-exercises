import random
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = [i.upper() for i in lower_letters]
symbols = ["'", "#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","]"]
numbers = ['1','2','3','4','5','6','7','8','9','0']
allchars = lower_letters.copy() + upper_letters.copy() + symbols.copy() + numbers.copy()

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




