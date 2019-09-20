<h1>Three methods of Normalizing misspelled words</h1>

<h3>
There are three python files and each of them represents a method of normalizing misspelled words.
These methods are imported from the package called "jellyfish" which is made by James Turk.
<br>
</h3>
<h4>
<ol>
  <li>Use "levenshtein_distance" to perform normalization.</li>
  <li>Use "damerau–Levenshtein_distance" to perform normalization.</li>
  <li>Use "damerau–Levenshtein_distance and Soundex" to perform normalization.</li>
</ol>
</h4>

<h3>
To test our program, we use three datasets to perform the task.
</h3>
<h4>
<ul>
  <li>misspell.txt</li>
  <li>correct.txt</li>
  <li>dict.txt</li>
</ul>
</h4>

<h4>
The whole process of running each python program:
</h4>
<h3>
<ol>
  <li>This program will first read the three files into three different lists, which are called misspell, correct, and dictionary.</li>
  <li>Then, for each token in misspell list, the program will run through the dictionary file to find the desired candidates that meet our requirement, which is the distance_limit.</li>
  <li>If the token in the dictionary meet our requirement, we will put it into a list called prediction.
After searching all the tokens in the dictionary, we will check whether our prediction list contains the corresponding correct word in correct list.</li>
</ol>
</h3>

<h4>
Output:<br>
While our program is checking through the tokens in the misspell list, our program will print all the words that our program couldn't successfully predict.
</h4>
For example:<br>
--------------------------------------------------------------------------------<br>
Misspell word:  wut<br>
The correct word:  what<br>
--------------------------------------------------------------------------------<br>

<h4>After all the misspell tokens have been visited, our program will print out the results of the test.</h4>

The example of the result is as follow:<br>
--------------------------------------------------------------------------------<br>
Prediction count: 28540<br>
Success predicted: 7858<br>
Tested size: 10322<br>
Recall: 76.1%<br>
Precision: 27.5%<br>
Not in dictionary: 1419<br>
--------------------------------------------------------------------------------<br>


