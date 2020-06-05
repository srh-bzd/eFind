"""
SYNOPSIS
    python3 efind.py

DESCRIPTION
    Count the number of words with and without one or more specified characters
    and return the words without the character(s) in the application or in a file (optional). 

PREREQUISITE
    - python 3
    - Gooey (https://github.com/chriskiehl/Gooey)
    - a list of words

AUTHOR
    Sarah Bouzidi
"""


from gooey import Gooey, GooeyParser
import argparse


def sortWords(fileIn, characters):
    """
    - open the file defined with the words
    - search for the words with and without the character(s)
    - create two lists of words :
        . one where the words have at least one of the characters
        . the other having the words without one of the characters
    - return the lists of words
    """  
    list_of_word_with = []
    list_of_word_without = []
    try:
        with open(fileIn, "r") as wordsInFile:
            for word in wordsInFile:
                word = word.strip()
                if any(character in word for character in characters):
                    list_of_word_with.append(word)
                else:
                    list_of_word_without.append(word)
            return list_of_word_with, list_of_word_without
    except IOError as erreur:
        print(erreur)
        exit(1)


def countWords(listsWords):
    """
    - count the number of words contained in each list (with len())
    - print the number
    """
    number_words_with_characters = len(listsWords[0])
    print("*----------------------------------------------------------------------")
    print("\nNumber of words with the character(s) : ", number_words_with_characters)
    number_words_without_characters = len(listsWords[1])
    print("Number of words without the character(s) : ", number_words_without_characters)


def writeWords(fileOut, listsWords):
    """
    - write an output file containing the list of words without the character(s) if user specified
    - or, basically, print the words without the character(s) 
    """
    if fileOut:
        if listsWords[1]:
            with open(fileOut, "w") as f:
                f.write("\n".join(listsWords[1]))
                print("\nThe file", fileOut, "was create.")
        else:
            print("\nNo need to create the file", fileOut, ". It would be empty.")
    else:
        print("\nWords without the character(s) :")
        print(*listsWords[1], sep="\n")
   

@Gooey(
    program_name="eFind",
    menu=[{
        'name': 'Menu',
        'items':[{
            'type':'AboutDialog',
            'menuTitle':'About',
            'name':'eFind',
            'description':'eFind is a program developed in python to count the number of words with and without one or more specified characters and return the words without the character(s). For more information : ',
            'website': 'https://github.com/srh-bzd/eFind',
            'developer': 'Sarah Bouzidi'
            },{
            'type':'MessageDialog',
            'menuTitle':'Information',
            'caption':'Information',
            'message':'eFind use Gooey to change the python script to a GUI application.'
            },{
            'type':'MessageDialog',
            'menuTitle':'Contact',
            'caption':'Contact',
            'message':'For any questions, additional information or otherwise, you can contact the developer via this email address : \nsarah.m.bouzidi@gmail.com'
            }]
            }])
def parseArgsCommandLine():
    """
    - define required and optional arguments in command-line
    - parse command-line
    - return the values of arguments
    """ 
    parser = GooeyParser(description='An easy way to find words')
    parser.add_argument("File", type = str, help = "Input file with the words list", widget='FileChooser')
    parser.add_argument("Characters", type = list, help = "Character(s) to find in words")
    parser.add_argument("--Write", type = str, help = "Output file with the words who hasn't the character(s)", widget='FileSaver')
    args = parser.parse_args()
    return args


def main():
    args = parseArgsCommandLine()
    listsWords = sortWords(args.File, args.Characters)
    countWords(listsWords)
    #By default, args.Write = None
    writeWords(args.Write,listsWords)


if __name__ == "__main__":
    main()
