'''To count total characters in file,
total words in file,
total lines in file
and frequency of given word in file.'''
 
from collections import Counter
def word_count(fname):
    count=0
    with open(fname,'r') as f:
        for line in f:
            word=line.split()
            count+=len(word)
    f.close()
    return count
        
def char_count(fname):
    count=0
    with open(fname,'r') as f:
        for line in f:
            word=line.split()
            count+=len(line)
    f.close()
    return count

def line_count(fname):
    count=0
    with open(fname,'r') as f:
        for line in f:
            word=line.split()
            count+=1
    f.close()
    return count

def freq_word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of characters in the file :\n",char_count("E:\\original.txt"))
print("Number of words in the file :\n",word_count("E:\\original.txt"))
print("Number of lines in the file :\n",line_count("E:\\original.txt"))
print("Number of words with frequency count in the file :\n",freq_word_count("E:\\original.txt"))
