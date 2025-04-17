from utils.text_utils import *
from utils.spacy_utils import *
from collections import Counter

import re
# import matplotlib.pyplot as plt
# import spacy

# nlp = spacy.load('en_core_web_lg')


split_sentences('to_use/1.txt', 'out/')


# def segment_sentences(in_path, out_path, count, nlp):
#     in_prefix = in_path.split('.')[0]
#     ext = in_path.split('.')[1]
#     for i in range(0, count):
#         filename = f'{in_prefix}{i}.{ext}'
#         try:
#             text = read_file(filename)
#         except:
#             print(f'cannot read: {filename}. Skipping...')
        
#         doc = nlp(text)
        
#         result = ''
#         for sent in doc.sents:
#             result += f'{sent.text}.\n\n'
#         out_filename = f'{out_path}{i}.{ext}'
#         write_file(result, out_filename)

# segment_sentences('expanded_transcripts/org_chem/calc2/.txt', 'ORG_CHEM_SENTENCE/', 1, nlp)
                
        
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