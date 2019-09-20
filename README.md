<h1>Three methods of Normalizing misspelled words</h1>

<h4>
There are three python files and each of them represents a method of normalizing misspelled words.
<br><br>
<ol>
  <li>Use levenshtein_distance to perform normalization.</li>
  <li>Use damerau–Levenshtein_distance to perform normalization.</li>
  <li>Use damerau–Levenshtein_distance and Soundex to perform normalization.</li>
</ol>
These methods are imported from the package called "jellyfish" which is made by James Turk.
</h4>

<h4>
To test our program, we use three datasets to perform the task.
<ul>
  <li>misspell.txt</li>
  <li>correct.txt</li>
  <li>dict.txt</li>
</ul>
</h4>

<h4>
The whole process of running each python program:<br>
<ol>
  <li>This program will first read the three files into three different lists, which are called misspell, correct, and dictionary.</li>
  <li>Then, for each token in misspell list, the program will run through the dictionary file to find the desired candidates that meet our requirement, which is the distance_limit.</li>
  <li>If the token in the dictionary meet our requirement, we will put it into a list called prediction.
After searching all the tokens in the dictionary, we will check whether our prediction list contains the corresponding correct word in correct list.</li>
</ol>
</h4>

<h4>
Output:
While our program is checking through the tokens in the misspell list, our program will print all the words that our program couldn't successfully predict.
</h4>
For example:<br>
--------------------------------------------------------------------------------<br>
Misspell word:  wut<br>
The correct word:  what<br>
--------------------------------------------------------------------------------<br>

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


