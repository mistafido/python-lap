import nltk
import string
from nltk import word_tokenize
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag

#read the file
file = open('nlp_wikipedia_sample.txt')
text = ''
for i in file.readlines():
    text += i
print(text)

#removing trailing spaces
trimmed_text = text.strip()
print(trimmed_text)

#convert to lowercase
converted_text = trimmed_text.lower()
print(converted_text)

#tokenization of the text using word tokenizer
tokenized_text = word_tokenize(converted_text)
print(tokenized_text)

#tokenization of text using word punt tokenizer
punct_tokenized_list = wordpunct_tokenize(converted_text)
print(punct_tokenized_list)

#get vocabulary
vocab_set = set(tokenized_text)
print(vocab_set)

#remove stop words
set_wo_stopwords = vocab_set - set(stopwords.words('english'))
print(set_wo_stopwords)

#remove punctuation
set_wo_punctuation = set_wo_stopwords - set(punctuation)
print(set_wo_punctuation)

#normalise the text using stemming and lemmartization
#stemming
stemmed_list = []
stemObj = SnowballStemmer('english')
for i in set_wo_punctuation:
    stemmed_list.append(i)
print(stemmed_list)

#parts of speech tagging
pos_tag_list = pos_tag(set_wo_punctuation)
print(pos_tag_list)

#for getting parts of speech
import nltk
nltk.download('wordnet')

def parts_of_speech(pos):
    if pos.startswith("N"):
        return wordnet.NOUN
    elif pos.startswith("J"):
        return wordnet.ADJ
    elif pos.startswith("V"):
        return wordnet.VERB
    elif pos.startswith("R"):
        return wordnet.ADV
    elif pos.startswith("S"):
        return wordnet.ADJ_SAT
    else:
        return ''
    

lemma_list = []
lemmaObj = WordNetLemmatizer()
for word,pos in pos_tag_list:
    get_pos = parts_of_speech(pos)
    if get_pos != '':
        lemma_list.append(lemmaObj.lemmatize(word, pos = get_pos))
    else:
        lemma_list.append(word)
print(lemma_list)

#creating ngrams for txt
from nltk import ngrams
bigrams = ngrams(set_wo_punctuation,2)
print(list(bigrams))


#Regular Expression processing
import re

sent3 = "1947 was when India became independent."
print("Occurences of a-z: ",re.search(r"[a-z]+",sent3)) 

sent3 = "1947 was when India became independent."
print("Occurences of 0-9: ",re.search(r"[0-9]+",sent3))

sent3 = "1947_was when India became independent."
print("Occurences of w and space: ",re.search(r"[\w ]+",sent3))

sent = "I like coffee" 
print(re.sub(r"coffee","tea",sent)) 

sent = "I like coffee and coffee is amazing. coffee keeps me awake. coffee is bad" 
print(re.findall(r"coffee",sent))

print(len(re.findall(r"coffee",sent)))