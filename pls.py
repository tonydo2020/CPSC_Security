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

    for a in len(string):


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
        getEncrypt(keylist,string):



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


