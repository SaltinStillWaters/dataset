from utils.text_utils import *
from utils.spacy_utils import *
from collections import Counter

import re
import matplotlib.pyplot as plt
import spacy

# nlp = spacy.load('en_core_web_lg')

# text = get_verbs_from_text(nlp, 'raws/.txt', 199)
# write_file(text, 'out.txt')

def clean_text(in_file, file_count):
    file_prefix = in_file.split('.')[0]
    file_ext = in_file.split('.')[1]
    for i in range (0, file_count):
        try:
            file_name = f'{file_prefix}{i}.{file_ext}'
            text = read_file(file_name)
        except:
            print(f'{file_name} does not exist. Skipping...')
            continue
        
        text = re.sub('Khan Academy ', '\n', text)
        write_file(text, file_name)
        continue
        text = re.sub(r'\s*\.', '.', text)
        text = re.sub(r'\. *', '.\n', text)
        text = re.sub(r', *', ', ', text)
        text = re.sub(r'  +', ' ', text)

        
clean_text('cleaned_raws/.txt', 200)
        
# # Split transcript into videos
# root = Path('raw_transcripts')

# text = read_file('raw_transcripts/prof_leonard/pre_calculus.txt')
# for i, vid in enumerate(text.split('\n\n')):
#     with open(f'expanded_transcripts/prof_leo/pre_cal/{i}.txt', 'w', encoding='utf-8') as f:
#         f.write(vid)

# nlp = spacy.load('en_core_web_lg')
# keywords = {"limit", "integral", "differentiate", "derive", "derivative", "integration", "integrate"}
# freqs = get_keywords(nlp, 'lime/.txt', 861, list(), keywords)
# write_file(freqs, 'out_freq.txt', 'w', '')


# nlp = spacy.load('en_core_web_lg')

# verbs = read_file('verbs_lemma').split()
# verb_counts = Counter(verbs).most_common()

# for verb, count in verb_counts:
#     write_file(f'{verb:<15}-{count}\n', 'verb_freq.txt', 'a', '')
    
    
    
# verbs = get_verbs(nlp, 'spacy_processing/docs/doc_all.spacy', 32, list())
# write_file(verbs, 'verbs_lemma')
# verb_counts = Counter(verbs).most_common()

# verbs, frequencies = zip(*verb_counts)

# plt.figure(figsize=(10, 5))
# plt.bar(verbs, frequencies, color='skyblue')
# plt.xlabel('Verbs')
# plt.ylabel('Frequency')
# plt.title('Verb Frequency')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()