Put all the dataset under the same path. Then run the .py files in order.

1.Global.py and Weighted.py
This is the Levenshtein distance for the MIDR of 0111 and 0113. Edit distance, also known as Levenshtein distance, the basic principle of the algorithm refers to the minimum number of edit operations required between two strings, from one to another, and the greater the distance, the more different they are. Licensed editing operations include replacing one character with another, inserting one character, and deleting one character. In this experiment, each word in misspell is first compared with each word in the dictionary and the editing distance is calculated. Then filter out the predicted words with the smallest edit distance. Finally, the correct spelling corresponding to the wrong word is compared with the predicted word. If they are consistent, the word is successfully corrected, and if it is inconsistent, it is a failure.
You can change the MIDR in Weighted multiply by number you want.

https://pypi.org/project/python-Levenshtein/
https://pypi.org/project/weighted-levenshtein/

2.ngram.py
The basic principle of the N-gram algorithm is: suppose there is a string S, then the N-gram of the string represents the segment obtained by dividing the original word by length N, that is, all substrings of length N in S. And we define N-gram distances based on non-repetitive Ngram participles. In this file, it calculates 2-Gram distance.

3.soundex and metaphone.py
The Soundex algorithm is an algorithm that converts any text string into a letter pattern that describes the phonetic representation. The algorithm considers similar pronunciation characters and bytes and is able to compare text pronunciations rather than letter comparisons. The Soundex method returns a four-character code representing the name, consisting of an English letter followed by three digits.
The Soundex reference rules are as follows:
b, f, p, v → 1
c, g, j, k, q, s, x, z → 2
d, t → 3
l → 4
m, n → 5
r → 6
https://en.wikipedia.org/wiki/Soundex

The Metaphone algorithm is mainly used for indexing English words or vocabulary pronunciation.
The Metaphone reference rules are as follows:
Drop duplicate adjacent letters, except for C.
If the word begins with 'KN', 'GN', 'PN', 'AE', 'WR', drop the first letter.
Drop 'B' if after 'M' at the end of the word.
'C' transforms to 'X' if followed by 'IA' or 'H' (unless in latter case, it is part of '-SCH-', in which case it transforms to 'K'). 'C' transforms to 'S' if followed by 'I', 'E', or 'Y'. Otherwise, 'C' transforms to 'K'.
'D' transforms to 'J' if followed by 'GE', 'GY', or 'GI'. Otherwise, 'D' transforms to 'T'.
Drop 'G' if followed by 'H' and 'H' is not at the end or before a vowel. Drop 'G' if followed by 'N' or 'NED' and is at the end.
'G' transforms to 'J' if before 'I', 'E', or 'Y', and it is not in 'GG'. Otherwise, 'G' transforms to 'K'.
Drop 'H' if after vowel and not before a vowel.
'CK' transforms to 'K'.
'PH' transforms to 'F'.
'Q' transforms to 'K'.
'S' transforms to 'X' if followed by 'H', 'IO', or 'IA'.
'T' transforms to 'X' if followed by 'IA' or 'IO'. 'TH' transforms to '0'. Drop 'T' if followed by 'CH'.
'V' transforms to 'F'.
'WH' transforms to 'W' if at the beginning. Drop 'W' if not followed by a vowel.
'X' transforms to 'S' if at the beginning. Otherwise, 'X' transforms to 'KS'.
Drop 'Y' if not followed by a vowel.
'Z' transforms to 'S'.
Drop all vowels unless it is the beginning.
https://en.wikipedia.org/wiki/Metaphone


https://pypi.org/project/jellyfish/










