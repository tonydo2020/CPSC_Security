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


def switch_state(argument):
    print("argument is:", argument)
    if int(argument) == 1:
        getString()
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


