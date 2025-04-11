from utils import *
import spacy


# with open('all_transcripts.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
#     print(len(text.split()))
#     quit()

# nlp = spacy.load('en_core_web_lg')

# instructions = set()
# for i in range(0, 32):
#     print(f'processing {i}')
#     doc = load_doc(f'docs/doc_all{i}.spacy', nlp)
#     for token in doc:
#         if token.pos_ == 'VERB':
#             instructions.add(token.text)
#     print(f'done processing {i}')

# with open('instructions_token.txt', 'w', encoding='utf-8') as f:
#     for i in instructions:
#         f.write(i + '\n')
# print(instructions)

# def chunk_text(text, chunk_size=400000):
#     return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# with open('all_transcripts.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
    
# chunks = chunk_text(text)
# for i, chunk in enumerate(chunks):
#     print(f'converting to doc {i}')
#     doc = nlp(chunk)
#     print(f'done converting to doc {i}')

#     print(f'saving to disk {i}')
#     save_doc_to_disk(doc, f'doc_all{i}.spacy')
#     print(f'done saving to disk {1}')