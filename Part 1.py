#Albert
#'Who said it' part 1

'''This code recieves a text and outputs each word in the code. If there are
repeating words, it would add 1 to the already existing word (making the amount
two and so on). At the end, it will output the total amount of words in the text.
'''

#This function removes punctuation, change letters to lowercase, and check if its string.

def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

#This function counts the amount of words and its repetition, and outputs it.

def get_counts(document):
    count = 0
    stored_words = {}
    every_word = []
    input_file = open(document)

#This loop stores the text in a variable
    
    text = ""
    for line in input_file:
        text = text + line + "\n"

    every_word = text.split()
    

#This loop, adds everything into a dictionary with the amount of that word repeated. It also counts the amount of words


    for word in every_word:
        word = normalize(word)
        if word != "":
            
            if word in stored_words:
                stored_words[word] = stored_words[word] + 1
                count = count + 1
            else:
                stored_words[word] = 1
                count = count +1
            

    stored_words["_total"] = count

    return stored_words

    input_file.close()

    
#This loops through the dictionary and prints the elements inside

william = get_counts("hamlet-short.txt")
jane = get_counts("pride-and-prejudice-short.txt")

for x in william:
    print (x + ": " + str(william[x]))

for x in jane:
    print (x + ": " + str(jane[x]))       

    
