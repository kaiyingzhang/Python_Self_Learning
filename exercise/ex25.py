#ex25 some basic practice
#functions of 1.split 2.sort 3. print

def break_words(stuff):
  words = stuff.split(' ')
  return words
  
def sort_words(words):
 return sorted(words)
 
def print_first_words(words):
 word = words.pop(0)
 print word
 
def sort_sentences(sents):
 sent = break_words(sents)
 return sent
 
def print_first_and_last_sentence(sentence):
 words = sort_sentences(sentence)
 print_first_words(words)
 