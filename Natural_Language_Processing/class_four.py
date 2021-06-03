#POS tagger
from nltk import word_tokenize
from nltk import pos_tag

sent1 = "The race officials refused to permit the team to race today"
print(pos_tag(word_tokenize(sent1)))

sent2 = "The gentleman wants some water to water the plants"
print(pos_tag(word_tokenize(sent2)))

text = word_tokenize("They refuse to permit us to obtain the refuse permit")
import nltk
print(nltk.pos_tag(text))

#Default taggeer 
import nltk
nltk.download('brown')
from nltk.corpus import brown

#getting the most common tag in the brown corpus
tags = [tag for (word,tag) in brown.tagged_words()]
most_common_tag = nltk.FreqDist(tags).max()
print(most_common_tag)

from nltk import DefaultTagger

barack = """Barack Hussein Obama (born August 4, 1961) is an American politician 
who served as the 44th President of the United States from January 20, 2009, to January 20, 2017.
A member of the Democratic Party, he was the first African American to assume the presidency 
and previously served as a United States Senator from Illinois (2005–2008)."""

tokenized_barack = word_tokenize(barack)
default_tagger = DefaultTagger(most_common_tag)
def_tagged_barack = default_tagger.tag(tokenized_barack)
print(def_tagged_barack)

#Lookup Tagger
#Ngram tagger
message = "the quick brown fox jumped over the lazy dog"
training_tag = pos_tag(word_tokenize(message))
print(training_tag)
#training the ngram tagger
ngram_tagger = nltk.NgramTagger(n=2,train=[training_tag])

message2 = "the lazy dog jumped over the quick brown fox"
message2_tags = ngram_tagger.tag(word_tokenize(message2))
print(message2_tags)

print(list(nltk.ngrams(pos_tag(word_tokenize(message)),n=2)))

#Unigram tagger 
barack = """Barack Hussein Obama II born August 4, 1961) is an American politician
who served as the 44th President of 
the United States from January 20, 2009, to January 20, 2017.
A member of the Democratic Party, he was the 
first African American to assume the presidency and previously
served as a United States Senator from Illinois (2005–2008)."""
bush = """George Walker Bush (born July 6, 1946) is an American politician who served as the 43rd President
 of the United States from 2001 to 2009.
He had previously served as the 46th Governor of Texas from 1995 to 2000.
Bush was born New Haven, Connecticut, and grew up in Texas. 
After graduating from Yale University in 1968 and Harvard Business School in 1975, he worked in the oil industry.
Bush married Laura Welch in 1977 and unsuccessfully ran for the U.S. House of Representatives shortly thereafter. 
He later co-owned the Texas Rangers baseball team before defeating Ann Richards in the 1994 Texas gubernatorial election. 
Bush was elected President of the United States in 2000 when he defeated Democratic incumbent 
Vice President Al Gore after a close and controversial win that involved a stopped recount in Florida. 
He became the fourth person to be elected president while receiving fewer popular votes than his opponent.
Bush is a member of a prominent political family and is the eldest son of Barbara and George H. W. Bush, 
the 41st President of the United States. 
He is only the second president to assume the nation's highest office after his father, following the footsteps
 of John Adams and his son, John Quincy Adams.
His brother, Jeb Bush, a former Governor of Florida, was a candidate for the Republican presidential nomination
 in the 2016 presidential election. 
His paternal grandfather, Prescott Bush, was a U.S. Senator from Connecticut."""
pos_tag_barack = pos_tag(word_tokenize(barack))
pos_tag_bush = pos_tag(word_tokenize(bush))
trump = """Donald John Trump (born June 14, 1946) is the 45th and current President of the United States.
Before entering politics, he was a businessman and television personality. 
Trump was born and raised in the New York City borough of Queens, and received an economics degree from the
 Wharton School of the University of Pennsylvania. 
He took charge of his family's real estate business in 1971, renamed it The Trump Organization, and expanded 
it from Queens and Brooklyn into Manhattan. 
The company built or renovated skyscrapers, hotels, casinos, and golf courses. 
Trump later started various side ventures, including licensing his name for real estate and consumer products.
He managed the company until his 2017 inauguration. 
He co-authored several books, including The Art of the Deal. He owned the Miss Universe and Miss USA beauty 
pageants from 1996 to 2015, and he produced and hosted the reality television show The Apprentice from 2003 to 2015.
Forbes estimates his net worth to be $3.1 billion."""

unigram_tag = nltk.UnigramTagger(train=[pos_tag_barack,pos_tag_bush])
trump_tags = unigram_tag.tag(word_tokenize(trump))
print(trump_tags)

#Tagging pipeline and backoff
default_tagger = DefaultTagger('NN')
patterns = [
    (r'.*\'s$','NN$'),     #possesive nouns
    (r'.*es$','VBZ'),      #3rd singular present 
    (r'^-?[0-9]+(.[0-9]+)?$','CD'),  #cardinal numbers
    (r'[Aa][Nn][Dd]','CC'),     #conjugate and
    (r'.*ed$','VBD'),      #simple past 
    (r',',','),            #comma
    (r'.*ould$','MD'),     #modals
    (r'.*ing$','VBG'),     #gerunds
    (r'.*s$','NNS'),       #plural nouns
]

regexp_tagger = nltk.RegexpTagger(patterns,backoff=default_tagger)
unigram_tag = nltk.UnigramTagger(train=[pos_tag_barack,pos_tag_bush],backoff=regexp_tagger)
trump_tags = unigram_tag.tag(word_tokenize(trump))
print(trump_tags)
