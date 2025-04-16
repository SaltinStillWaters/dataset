import utils
from pathlib import Path
import re


# def clean_text(in_file, file_count):
#     file_prefix = in_file.split('.')[0]
#     file_ext = in_file.split('.')[1]
#     for i in range (0, file_count):
#         try:
#             file_name = f'{file_prefix}{i}.{file_ext}'
#             text = read_file(file_name)
#         except:
#             print(f'{file_name} does not exist. Skipping...')
#             continue
        
#         text = re.sub(r'\n', ' ', text)
#         text = re.sub(r'\s*\.', '.', text)
#         text = re.sub(r'\. *', '.\n', text)
#         text = re.sub(r', *', ', ', text)
#         text = re.sub(r'  +', ' ', text)

#         write_file(text, file_name)
        
# clean_text('raws/.txt', 2)

#Split transcripts for each video

# #prof_leonard
# utils.split_transcripts(r'raw_transcripts\prof_leonard\calculus_1.txt', r'raw_transcripts\prof_leonard\calculus_1')
# utils.split_transcripts(r'raw_transcripts\prof_leonard\calculus_2.txt', r'raw_transcripts\prof_leonard\calculus_2')
# utils.split_transcripts(r'raw_transcripts\prof_leonard\differential_eqs.txt', r'raw_transcripts\prof_leonard\differential_eqs')
# utils.split_transcripts(r'raw_transcripts\prof_leonard\pre_calculus.txt', r'raw_transcripts\prof_leonard\pre_calculus')

#organic chem
#utils.split_transcripts(r'raw_transcripts\organic_chem\calculus_2.txt', r'raw_transcripts\organic_chem\calculus_2')

#khan
#utils.split_transcripts(r'raw_transcripts\khan\calculus.txt', r'raw_transcripts\khan\calculus')


