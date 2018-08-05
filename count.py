'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
    dictionary = {}

    for char in text:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    for key, value in dictionary.items():
        print(key, value)
    '''letter = input(
    for char in text:
    text.count('letter')


    repeats =
    print("{} {}",format(letter), format(repeats))''' 
   
    # add your code here

def count_char_insensitive(text):
    dictionary = {}

    for char in text:
        if char.lower() in dictionary:
            dictionary[char.lower()] += 1
        else:
            dictionary[char.lower()] = 1

    for key, value in dictionary.items():
        print(key, value)
    # add your code here

# bonus task:
def count_char_ordered(text):
    dictionary = {}

    for char in text:
        if char.lower() in dictionary:
            dictionary[char.lower()] += 1
        else:
            dictionary[char.lower()] = 1

    sorted_by_value = sorted(dictionary.items(), key=lambda i:i[1], reverse=True)
    for key, value in sorted_by_value:
        print(key, value)
    # add your code here 

text1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy' # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text2)
count_char_insensitive(text2)
count_char_ordered(text2)

