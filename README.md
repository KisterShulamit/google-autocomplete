# GOOGLE AUTOCOMPLETE PROJECT
## Project target:
Displaying the input of the five most relevant completion from a given database (text files in a folder tree structure)
## Implementation :
#### DATABASE:
--Dictionary of sentences:Each member is: a sentence, the name of the file from which it was taken, its line number in
#### Dictionary of word:
Key - the wordValue - The indexes are from the Dictionary of the sentences in which the word appears
#### First stage:
Read the files into the database
#### Second stage:
The system waits for input from the user, the system ignores punctuation in the textFor each of the words in the text we will take the sentences in which it is according to the databaseTo support the possibility of spelling errors in the input or return sentences with similar input when the input is not found:We have created a dictionary that contains as a key all the variations of the word - deleting each of the letters, replacing each of the letters with each of the letters abc.. , and inserting each of the abc.. letters between each of the two letters of the word.Each of the variations of the word has a score according to the originalAccording to this we will return the 5 sentences with the highest score.

In order to support the possibility of giving priority to sentences in which appear in the sequence of words as the sequence entered by the user we did something that makes the search significantly longer so this is a point we would like to improve on our program.(Just to note that without this feature the search takes a split second)

## Running example:
Loading the files and preparing the program....
The program is ready
Enter your sentence: Python
You have 5 suggests:
1   the 'r' and 'w' modes (will be an error in future Python releases). (changelog 1)
2 The functions in this chapter interact with Python objects regardless (abstract 1)
3 "logging" --- Logging facility for Python (logging 1)
4 for which they do not apply, they will raise a Python exception. (abstract 1)
5 evaluating expression strings using the Python literal syntax.  The (3 1)
Python is
You have 5 suggests:
1       are not supported if Python is configured using "--without- (init_config 1)
2       The option is ignored if Python is built using "--without- (init_config 1)
3 * "Main" initialization phase, Python is fully initialized: (init_config 1)
4 embedding Python is less straightforward than writing an extension. (intro 1)
5    If Python is built without docstrings, the value will be empty. (intro 1)
Python is#
Enter your sentence:

