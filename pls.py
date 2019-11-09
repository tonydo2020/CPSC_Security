import random

D = [('F','P','Z'),
     ('G','Q'),
     ('I','S'),
     ('J','T'),
     ('A','K','U'),
     ('B','L','V'),
     ('C','M','W'),
     ('D','N','X'),
     ('E','O','Y'),

     ]

symbol_list = ['!', '@', '#', '$','%']

def getString():
    user_string = input("Enter in your string")
    return user_string


def displayPlainText():
    print("b")


def displayText():
    print("c")


def Quit():
    quit()


def cypher(user_string):
    print("a")
    

def encrypt( k, string):
    print("d")


def getKey():
    number = random.randint(0,4)
    return symbol_list[number]


def getEncrypt(keylist, string):
    pkey =""
    pkey_count = 0
    c = ""

    for a in range(len(keylist)):
        c = keylist[a]
        if c == '(':
            pkey = keylist[a + 1]
            break

    for b in range(len(keylist)): # starting at the next key value after the (
        if keylist[b] == pkey:
            pkey_count = pkey_count + 1

    encrypt_string(pkey, pkey_count, keylist, string)


def encrypt_string(pkey, pkey_count, keylist, string):

    if pkey == '!':
        outer_list = []

        b = 0
        for a in range(pkey_count):
            if keylist[a] == '!':
                inner_list = []
                while string[b] != "":
                    if ord(string[b]) < 222:
                        inner_list.append('+')
                        string[b] = chr(ord(string[b] + 33))
                        b += 1
                    else:
                        inner_list.append('-')
                        string[b] = chr(ord(string[b] - 33))
                        b += 1
                print("inner list is: ", inner_list)

                #for b in len(string):
                 #   list[b] = chr(ord(string[b] + 33)) + '+'



    #elif pkey == '@':
    #elif pkey == '#':
    #elif pkey == '$':
    #elif pkey == '%':
    #else:


def switch_state(argument):
    print("argument is:", argument)
    if int(argument) == 1: # THIS IS ARGUMENT 1
        string = getString()
        print("Received String is: ", string)
        length = random.randint(1,10)
        keylist = ""
        for a in range(length):
            keylist += getKey()

        keylist = '(' + keylist + ')'
        print(keylist)
        #print("keylist is: (" + keylist + ")")
        getEncrypt(keylist,string)



    elif int(argument) == 2:
        displayPlainText()
    elif int(argument) == 3:
        displayText()
    else:
        Quit()


def main():
    run = True
    while run:
        print("1 Encrypt Text")
        print("2 Decrypt Text")
        print("3 Print Encrypted")
        print("Anything else to quit")
        user_input = input("Please enter an option\n")
        switch_state(user_input)
        if user_input == 4:
            run = False


if __name__ == "__main__":
    main()


