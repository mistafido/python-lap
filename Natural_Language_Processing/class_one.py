import nltk
from nltk import *
sent = 'India is a republic nation, we are proud Indians'

print(len(sent))
print(sent[0:5])
print(sent[11:19])

import nltk
nltk.download('punkt')

print(nltk.word_tokenize(sent))

tokens = nltk.word_tokenize(sent)
vocab = sorted(set(tokens))
print(vocab)

from string import punctuation
vocab_wo_punc = []
for i in vocab:
  if i not in punctuation:
    vocab_wo_punc.append(i)
print(vocab_wo_punc)

#parts of speech
import nltk
nltk.download('averaged_perceptron_tagger')

from nltk import pos_tag
pos_list = pos_tag(vocab_wo_punc)
print(pos_list)

#Rooting of a word: stemming
from nltk.stem.snowball import SnowballStemmer
stemObj = SnowballStemmer('english')
stemObj.stem('studying')

stemmed_vocab = []
stemObj = SnowballStemmer('english')
for i in vocab_wo_punc:
  stemmed_vocab.append(stemObj.stem(i))
print(stemmed_vocab)

#Base of a word: Lemmatization
import nltk
nltk.download('wordnet')

from nltk.stem.wordnet import WordNetLemmatizer
lemmaObj = WordNetLemmatizer()
lemmaObj.lemmatize("went",pos='v')

#stop words
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
wo_stop_words = []
stop_words_set = set(stopwords.words('english'))
for i in vocab_wo_punc:
  if i not in stop_words_set:
    wo_stop_words.append(i)
print(wo_stop_words)

#Distribution and ngrams
#frequency distribution
text = 'I saw John coming. He was with mary. I talked to John and Mary \
John said he met Mary on the way. John and Mary were going to school.'
print(nltk.FreqDist(nltk.word_tokenize(text)))
nltk.FreqDist(text.split()).plot()

#conditional frequency distribution
cfd = nltk.ConditionalFreqDist(
    (a,b)
    for a in brown.categories()
    for b in brown.words(categories=genre))
genres_list = ['romance','news','science_fiction','humor','religion','hobbies']
modals_list = ['may','could','can','must','will','might']
cfd.tabulate(conditions=genres_list, sample=modals_list)

#ngrams
from nltk import ngrams
bigrams = ngrams(vocab_wo_punc,2)
print(list(bigrams))

trigrams = ngrams(vocab_wo_punc,3)
print(list(trigrams))