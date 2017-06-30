
""" Program for 2.7 Python 
Text content analyser, analyzes input from a file, compiles statistics on it: 
1)total word count, 2) count of unique words, 3)number of sentences, 4)average
sentence lenght in words, 5) list of words used, in order of descending 
frequency."""

import sys, re
from collections import defaultdict, Counter
from operator import itemgetter

#opens incoming txt file, for reading
if len(sys.argv) < 2: 
	print "Please supply a filename in txt format, with program."
	exit(1)
else: 
	f = open (sys.argv[1]).read()

#cleans file for analysis
content = str(f)
content = content.lower()
content = content.replace(".", "")
content = content.replace(",", "")
content = content.replace("!", "")
content = content.replace("?", "")

d = defaultdict(int)
for word in content.split(): 
	d[word]+= 1
	distinct_word = d.items()

print "\nFile Contains"
print "Total Word Count: ", len(content.split())
print "Unique Word Count: ", len(distinct_word)

sentences = [s.strip() for s in re.split('[\.\?\!]', f) if s]
print "Number of Sentences: ", int(len(sentences))

print "Average Word Count in Sentence: ", int(len(content.split())/len(sentences))

print "Word Frequency Use in Descending Order: "
s = sorted(d.items(), key = itemgetter(1), reverse = True)
for k, (words, count) in enumerate(s): 
	print (words, count)	
