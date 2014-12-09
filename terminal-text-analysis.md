Terminal Text Analysis
======================

**locate**

find filenames quickly

**find**

also locates files

example: find / -name foo
finds foo

find . -name foo\*bar
find any filename that begins with foo and ends with bar

**grep**

Searches text or searches the given file for lines containing a match to the given strings or words.

Syntax
grep 'word' filename
grep 'word' file1 file2 file3
grep 'string1 string2'  filename
cat otherfile | grep 'something'

You can force grep to ignore word case i.e match boo, Boo, BOO and all other combination with the -i option:
grep -i "boo" /etc/passwd

Use grep to search 2 different words
egrep -w 'word1|word2' /path/to/file

**sed**

automatically 

A simple example is changing "day" in the "old" file to "night" in the "new" file:

sed s/day/night/ <old >new

to save file:

echo day | sed s/day/night/ 

**wc**

print the number of bytes, words, and lines in files  

-c, --bytes
print the byte counts

-m, --chars
print the character counts

-l, --lines
print the newline counts

-L, --max-line-length
print the length of the longest line

-w, --words
print the word counts

**uniq**

remove duplicate lines from a sorted file  

-c, --count
prefix lines by the number of occurrences

-d, --repeated
only print duplicate lines

-D, --all-repeated[=delimit-method] print all duplicate lines
delimit-method={none(default),prepend,separate} Delimiting is done with blank lines.

-f, --skip-fields=N
avoid comparing the first N fields

-i, --ignore-case
ignore differences in case when comparing

-s, --skip-chars=N
avoid comparing the first N characters

-u, --unique
only print unique lines

-w, --check-chars=N
compare no more than N characters in lines

**sort**

sort lines of text files

