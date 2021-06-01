#Parts of Speech using chunking techniques
from nltk import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk

import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')

barack = """Barack Hussein Obama (born August 4, 1961) is an American politician 
who served as the 44th President of the United States from January 20, 2009, to January 20, 2017.
A member of the Democratic Party, he was the first African American to assume the presidency 
and previously served as a United States Senator from Illinois (2005–2008)."""

tokenized_barack = word_tokenize(barack)
pos_list = pos_tag(tokenized_barack)
print(ne_chunk(pos_list))

from nltk import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser

barack = """Barack Hussein Obama (born August 4, 1961) is an American politician 
who served as the 44th President of the United States from January 20, 2009, to January 20, 2017.
A member of the Democratic Party, he was the first African American to assume the presidency 
and previously served as a United States Senator from Illinois (2005–2008)."""

grammar = r"""Place: {<NNP><NNPS>+}
           Date: {<NNP><CD><,><CD>}
           Person: {<NNP>+}
           """
           
tokenized_barack = word_tokenize(barack)
pos_list = pos_tag(tokenized_barack)
regParser = RegexpParser(grammar)
regLines = regParser.parse(pos_list)
print(regLines)

text = """The Sansad Bhavan (Parliament House) is located in New Delhi. It was designed by Edwin Lutyens and Herbert Baker, who were responsible for planning and construction of New Delhi by British government. The construction of buildings took six years and the opening ceremony was performed on 18 January 1927 by the then Viceroy and Governor-General of India, Irwin. 
In November 2014, Zomato completed another round of funding of US$60 million at a post-money valuation of ~US$660 million. This round of funding was being led jointly by Info Edge India and Vy Capital, with participation from Sequoia Capital. To contact reach us at +61 450 266 295.
Uber Technologies Inc. (doing business as Uber) is a peer-to-peer ridesharing, taxi cab, food delivery, bicycle-sharing, and transportation network company (TNC) headquartered in San Francisco, California, with operations in 785 metropolitan areas worldwide. Its platforms can be accessed via its websites and mobile apps. Uber has been prominent in the sharing economy, so much so that the changes in industries as a result of it have been referred to as Uberisation. 
Justdial is an Indian-based search services company founded by Venkatachalam Sthanu Subramani Mani. The company's headquarters is in Mumbai, Maharashtra, India. It has offices in Ahmedabad, Bangalore, Chandigarh, Chennai, Coimbatore, Delhi, Hyderabad, Jaipur, Kolkata and Pune.[8] Just Dial was in news on November 10, 2017 for expected acquisition by Google and based on this news the share prices at NSE rose about 20%. Customerservice number 88888 88888.
An earthquake (also known as a quake, tremor or temblor) is the shaking of the surface of the Earth, resulting from the sudden release of energy in the Earth's lithosphere that creates seismic waves. Earthquakes can range in size from those that are so weak that they cannot be felt to those violent enough to toss people around and destroy whole cities. The seismicity, or seismic activity, of an area is the frequency, type and size of earthquakes experienced over a period of time. The word tremor is also used for non-earthquake seismic rumbling. Dates of the recent earthquakes that occured this year 7-Sep-18, 6-September-18, September 05,2018, 29-08-18, 25/Aug/18 and many more.
"""

grammar = r"""Place: {<NNP><NNPS>+}
           Date: {<NNP><CD><,><CD>}
           Person: {<NNP>+}
           Organisation: {<NNP><NNP>}
           """
           
tokenized_text = word_tokenize(text)
pos_list = pos_tag(tokenized_text)
reg_parser = RegexpParser(grammar)
reg_lines = reg_parser.parse(pos_list)
print(reg_lines)