Lab Notes
Matt Fernandez
=====================

**Basic Terminal Shortcuts Basic file manipulation**

CTRL L = Clear the terminal cat <fileName> = show content of file
CTRL D = Logout (less, more)
SHIFT Page Up/Down = Go up/down the terminal head = from the top
CTRL A = Cursor to start of line -n <#oflines> <fileName>
CTRL E = Cursor the end of line
CTRL U = Delete left of the cursor tail = from the bottom
CTRL K = Delete right of the cursor -n <#oflines> <fileName>
CTRL W = Delete word on the left
CTRL Y = Paste (after CTRL U,K or W) mkdir = create new folder
TAB = auto completion of file or command mkdir myStuff ..
CTRL R = reverse search history mkdir myStuff/pictures/ ..
!! = repeat last command
CTRL Z = stops the current command (resume with fg in foreground or bg in background) cp image.jpg newimage.jpg = copy and rename a file

**Basic Terminal Navigation**

cp image.jpg <folderName>/ = copy to folder
cp image.jpg folder/sameImageNewName.jpg
ls -a = list all files and folders cp -R stuff otherStuff = copy and rename a folder
ls <folderName> = list files in folder cp *.txt stuff/ = copy all of *<file type> to folder
ls -lh = Detailed list, Human readable
ls -l *.jpg = list jpeg files only mv file.txt Documents/ = move file to a folder
ls -lh <fileName> = Result for file only mv <folderName> <folderName2> = move folder in folder
mv filename.txt filename2.txt = rename file
cd <folderName> = change directory mv <fileName> stuff/newfileName
if folder name has spaces use “ “ mv <folderName>/ .. = move folder up in hierarchy
cd / = go to root
cd .. = go up one folder, tip: ../../../ rm <fileName> .. = delete file (s)
rm -i <fileName> .. = ask for confirmation each file
du -h: Disk usage of folders, human readable rm -f <fileName> = force deletion of a file
du -ah: “ “ “ files & folders, Human readable rm -r <foldername>/ = delete folder
du -sh: only show disc usage of folders
touch <fileName> = create or update a file
pwd = print working directory
ln file1 file2

**Researching Files Extract, sort and filter data**

grep <someText> <fileName> = search for text in file
  -i = Doesn't consider uppercase words
locate <text> = search the content of all the files -I = exclude binary files
locate <fileName> = search for a file grep -r <text> <folderName>/ = search for file names
sudo updatedb = update database of files with occurrence of the text
find = the best file search tool (fast) With regular expressions:
find -name “<fileName>”
find -name “text” = search for files who start with the word text grep -E ^<text> <fileName> = search start of lines
find -name “*text” = “ “ “ “ end “ “ “ “ with the word text
grep -E <0-4> <fileName> =shows lines containing numbers 0-4
grep -E <a-zA-Z> <fileName> = retrieve all lines
with alphabetical letters
Search from file Size (in ~)
find ~ -size +10M = search files bigger than.. (M,K,G) sort = sort the content of files
sort <fileName> = sort alphabetically
Search from last access sort -o <file> <outputFile> = write result to a file
find -name “<filetype>” -atime -5 sort -r <fileName> = sort in reverse
('-' = less than, '+' = more than and nothing = exactly) sort -R <fileName> = sort randomly
sort -n <fileName> = sort numbers
Search only files or directory’s
find -type d --> ex: find /var/log -name "syslog" -type d wc = word count
find -type f = files wc <fileName> = nbr of line, nbr of words, byte size
-l (lines), -w (words), -c (byte size), -m
More info: man find, man locate (number of characters)
cut = cut a part of a file
-c --> ex: cut -c 2-5 names.txt
(cut the characters 2 to 5 of each line)
-d (delimiter) (-d & -f good for .csv files)
-f (# of field to cut)
more info: man cut, man sort, man grep