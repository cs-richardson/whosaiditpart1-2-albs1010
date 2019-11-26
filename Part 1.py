#Albert
#'Who said it' part 1

'''This code recieves a text and outputs each word in the code. If there are
repeating words, it would add 1 to the already existing word (making the amount
to). At the end, it will output the total amount of words in the text.
'''

#This function removes punctuation, change letters to lowercase, and check if its string.

def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

#This function counts the amount of words and its repetition, and outputs it.

def get_counts(document):
    count = 0
    word = {}
    every_word = []
    input_file = open(document)

#This loop stores the text in a variable
    
    text = ""
    for line in input_file:
        text = text + line + "\n"

    every_word = text.split()
    

#This loop, after each word is stored in a list, adds everything into a dictionary with the amount of that word repeated


    for i in every_word:
        i = normalize(i)
        if i in word:
            word[i] = word[i] + 1
        else:
            word[i] = 1

#The code below prints each element in the dictionary as well as the total amount of words
            
    for x in word:
        if x != "":
            print (x + ": " + str(word[x]))
            count = count + word[x]

    print("Total: " + str(count))

    input_file.close()


get_counts("hamlet-short.txt")
get_counts("pride-and-prejudice-short.txt")
    
