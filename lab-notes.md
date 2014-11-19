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

Commands for moving around the filesystem include the following.

- pwd: The pwd command allows you to know the directory in which you're located (pwd stands for "print working directory"). For example, pwd in the desktop directory will show ~/Desktop. Note that the GNOME terminal also displays this information in the title bar of its window.
- cd: The cd command allows you to change directories. When you open a terminal, you will be in your home directory. To move around the filesystem, use cd.
- To navigate to your desktop directory, use cd ~/Desktop
- To navigate into the root directory, use cd /
- To navigate to your home directory, use cd
- To navigate up one directory level, use cd ..
- To navigate to the previous directory (or back), use cd -
- To navigate through multiple levels of directories at once, use cd /var/www, for example, which will take you directly to the /www subdirectory of /var.

**Manipulating Files and Folders**

You can manipulate files and folders by using the following commands.

- cp: The cp command makes a copy of a file for you. For example, cp file foo makes an exact copy of the file whose name you entered and names the copy foo, but the first file will still exist with its original name. After you use mv, the original file no longer exists, but after you use cp, that file stays and a new copy is made.
- mv: The mv command moves a file to a different location or renames a file. Examples are as follows: mv file foo renames the original file to foo. mv foo ~/Desktop moves the file foo to your desktop directory but does not rename it. You must specify a new filename to rename a file.
To save on typing, you can substitute ~ in place of the home directory. Note: If you are using mv with sudo, you will not be able to use the ~ shortcut. Instead, you will have to use the full pathnames to your files.
- rm: Use this command to remove or delete a file in your directory. It does not work on directories that contain files.
- ls: The ls command shows you the files in your current directory. Used with certain options, it lets you see file sizes, when files where created, and file permissions. For example, ls ~ shows you the files that are in your home directory.
- mkdir: The mkdir command allows you to create directories. For example, mkdir music creates a music directory.

**Pandoc**
pandoc -o output.html input.txt
pandoc test.txt -o test.pdf
pandoc -f html -t markdown http://www.fsf.org
pandoc -o hello.tex hello.txt

**Grep**
- egrep or grep -E
- Run grep with extended regular expressions.
-i
Ignore case (ie uppercase, lowercase letters).
- -v
Return all lines which don't match the pattern.
- -w
Select only matches that form whole words.
- -c
Print a count of matching lines.
- Can be combined with the -v option to print a count of non matchine lines.
- -l
Print the name of each file which contains a match.
Normally used when grep is invoked with wildcards for the file argument.
- -n
Print the line number before each line that matches.
- -r
Recursive, read all files in given directory and subdirectories.

**Git**

- git init
- git add
- git push
- git commit
- git origin -u committ