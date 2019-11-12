import random

D = [('F', 'P', 'Z'),
     ('G', 'Q'),
     ('I', 'S'),
     ('J', 'T'),
     ('A', 'K', 'U'),
     ('B', 'L', 'V'),
     ('C', 'M', 'W'),
     ('D', 'N', 'X'),
     ('E', 'O', 'Y'),

     ]

symbol_list = ['!', '@', '#', '$', '%']


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


def encrypt(k, string):
    print("d")


def getKey():
    number = random.randint(0, 4)
    return symbol_list[number]


def getEncrypt(keylist, string):
    pkey = ""
    pkey_count = 0
    c = ""

    for a in range(len(keylist)):
        c = keylist[a]
        if c == '(':
            pkey = keylist[a + 1]
            break

    for b in range(len(keylist)):  # starting at the next key value after the (
        if keylist[b] == pkey:
            pkey_count = pkey_count + 1
    operation_list = []
    for a in range(pkey_count):
        string = encrypt_string(pkey, pkey_count, keylist, string, operation_list)

    print("operation list is: ", operation_list)

    fully_encrypt_list = []
    fully_encrypt_string = ""
    for a in range(len(string)):
        fully_encrypt_string += string[a]
        for b in range(len(operation_list[a])):
            fully_encrypt_string += operation_list[a][b]

    print("fully_encrypt_string: ", fully_encrypt_string)
def append_character_exclam(character, position, inner_list, rule_list):
    if character == '+' or character == '-':
        return
    elif ord(character) < 222:
        num = ord(character) + 33
        num_char = chr(num)
        inner_list.insert(position + 1, num_char)
        rule_list.insert(position + 1, '+')
    elif ord(character) > 222:
        num = ord(character) - 33
        num_char = chr(num)
        inner_list.append(num_char)
        rule_list.append('-')


def encrypt_string(pkey, pkey_count, keylist, string, operation_list):
    print("pkey_count is: ", pkey_count)
    encrypted_string = ""
    print("passed string is: ", string)
    for a in range(pkey_count):
        if pkey == '!':
            if keylist[a + 1] == '!':
                print("here")
                inner_list = []
                rule_list = []
                counter = 0
                for b in string:
                    append_character_exclam(b, counter, inner_list, rule_list)
                    counter += 1
                print("inner list is: ", inner_list)
                print("rule list is: ", rule_list)

                for a in range(len(inner_list)):

                    encrypted_string += inner_list[a]

                operation_list.append(rule_list)
                print("encrypted string is: ", encrypted_string)
                return encrypted_string

def switch_state(argument):
    print("argument is:", argument)
    if int(argument) == 1:  # THIS IS ARGUMENT 1
        string = getString()
        print("Received String is: ", string)
        length = random.randint(1, 10)
        keylist = ""
        for a in range(length):
            keylist += getKey()

        keylist = '(!!!' + keylist + ')'
        print(keylist)
        # print("keylist is: (" + keylist + ")")
        getEncrypt(keylist, string)



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


