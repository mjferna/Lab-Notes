Pandoc commands
=================

**Installing Pandoc**
sudo ln -s /usr/lib/rstudio/bin/pandoc/pandoc /usr/local/bin
sudo ln -s /usr/lib/rstudio/bin/pandoc/pandoc-citeproc /usr/local/bin

**Remember to install LaTeX**
 apt-get install texlive
 
http://johnmacfarlane.net/pandoc/installing.html

**Using Pandoc**

pandoc -o output.html input.txt

To convert hello.html from html to markdown:
pandoc -f html -t markdown hello.html

to convert it to PDF:
pandoc test.txt -o test.pdf

http://johnmacfarlane.net/pandoc/getting-started.html
