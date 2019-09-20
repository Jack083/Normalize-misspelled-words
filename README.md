<h1>Three different ways of Normalizing misspelled words</h1>

<h4>
These three python files implement three different methods, which are levenshtein_distance,damerau–Levenshtein_distance and Soundex.
These methods are imported from the package called "jellyfish" which is made by James Turk.
</h4>

<h4>
All these python files use similar process to the run the test.
Input:
There are three inputs for this program, which are
1. misspell.txt
2. correct.txt
3. dict.txt
</h4>

<h4>
Process:
This program will first read the three files into three different lists, which are called misspell, correct, and dictionary.
Then, for each token in misspell list, the program will run through the dictionary file to find the desired candidates that meet our requirement, which is the distance_limit.
If the token in the dictionary meet our requirement, we will put it into a list called prediction.
After searching all the tokens in the dictionary, we will check whether our prediction list contains the corresponding correct word in correct list.
</h4>

<h4>
Output:
While our program is checking through the tokens in the misspell list, our program will print all the words that our program couldn't successfully predict.
</h4>
For example:
--------------------------------------------------------------------------------
Misspell word:  wut
The correct word:  what
--------------------------------------------------------------------------------

<h4>After all the misspell tokens have been visited, our program will print out the results of the test.</h4>

The example of the result is as follow:
--------------------------------------------------------------------------------
Prediction count: 28540
Success predicted: 7858
Tested size: 10322
Recall: 76.1%
Precision: 27.5%
Not in dictionary: 1419
--------------------------------------------------------------------------------


