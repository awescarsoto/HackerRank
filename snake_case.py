'''
Alice is learning English and wants to keep track of all of the new words she learns. Being a programmer, Alice decides to put all of her words into one string, , where each word is separated by a single underscore character. This is known as Snake Case. Can you determine the number of words in Alice's string?

Given , print the total number of underscore-delimited words it contains on a new line.

Note: You simply need to count the number of words; do not concern yourself with whether or not the words are distinct.

Input Format

A single line containing string .

Constraints

Each word in  consists of one or more lowercase English alphabetic letters.
All words in  are delimited by single underscores (_).
Output Format

Print the number of underscore-delimited words in string .

Sample Input 0

have_a_nice_day
Sample Output 0

4
Explanation 0

image

String  contains four words:

have
a
nice
day
Thus, we print  on a new line.
'''
s = raw_input().strip()
if len(s) == 0:
    print 0
else:
    underscores = 0
    for letter in s:
        if letter == "_":
            underscores += 1
    print (underscores + 1)