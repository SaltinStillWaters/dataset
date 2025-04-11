from utils.text_utils import *
from utils.spacy_utils import *
import spacy

nlp = spacy.load('en_core_web_lg')
text = read_file('spacy_processing/test.txt')
doc = nlp(text)

result = set()
for token in doc:
    if token.pos_ == 'VERB':
        result.add(token.text)

print(result)