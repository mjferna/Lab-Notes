##An attempt at a word count application via terminal

import os

name = raw_input('Hey there! What\'s your name?\n')
print 'Nice to meet you, {0}.'.format(name)
print 'Welcome to TextsCount!'
print 'This program counts the number of words, lines, and sentences in a given text file.'
lines, blanklines, sentences, words = 0, 0, 0, 0
print '-' * 50
filename = raw_input('Choose a file by typing its path!\n')
try:
  textf = open('{0}'.format(filename), 'r')
except IOError:
  print 'Cannot open file %s for reading' % filename
  import sys
  sys.exit(0)

for line in textf:
  print line,
  lines += 1
  
  if line.startswith('\n'):
    blanklines += 1
  else:
    sentences += line.count('.') + line.count('!') + line.count('?')
    tempwords = line.split(None)
    print tempwords
    words += len(tempwords)

    
textf.close()
os.system('clear')

print 'Here you are, {0}!'.format(name)

print '-' * 50
print "Lines      : ", lines
print "Blank lines: ", blanklines
print "Sentences  : ", sentences
print "Words      : ", words
