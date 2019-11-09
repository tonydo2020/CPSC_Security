import random

#List of keys and alphabet
ciphers = ['!','@','#','$','%','^','&','*','(',')','-','=','~']

num_con = [['F','P','Z'],
     ['G','Q'],
     ['H','R'],
     ['I','S'],
     ['J','T'],
     ['A','K','U'],
     ['B','L','V'],
     ['C','M','W'],
     ['D','N','X'],
     ['E','O','Y'],
     
    ]
def valid_key(key):
    if key not in ciphers:
        print("Invalid key")
        
    
def get_key_value(key):
    counter = 0 
    for a in ciphers:
        if a == key:
            return counter
        else:
            counter = counter +1

def main():
    #Testing with raw values for now
    test_input = input("Enter your message")

    key = (input("Enter your key: "))
    # key = !
    key_value = get_key_value(key)
    print("Key_value: ", key_value)
        
    #Testing with actual files

    #file_name = input("Enter in the file's name")
    #file_input = open(file_name,"r")

    string_output = ""
    size_of_string = ""
    for i in range(len(test_input)):
        character = test_input[i]
        
        char_con = int(character)
        print("char con is: ", char_con)
        #location = alphabets.find(character)
        size_of_string = (len(num_con[char_con + key_value % 10]) - 1)
        print("size of string is: ", size_of_string)
        rand = random.randint(0,size_of_string)
        print(num_con[char_con][rand])
        
        #new_location = (location + key) % 26
        #string_output += alphabets[new_location]
        #print("new character and location", alphabets[new_location], new_location)
        
        string_output += (num_con[char_con][rand])
        print("original input: ", test_input)
        print("encrpyted output: ", string_output)

if __name__ == '__main__':
    main()
