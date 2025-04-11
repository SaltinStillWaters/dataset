from utils.text_utils import *
from spacy.tokens import Doc

def save_doc_to_disk(doc, out_file):
    doc.to_disk(Path(out_file))

def load_doc(in_file, nlp):
    return Doc(nlp.vocab).from_disk(in_file)

def get_word_count(in_file):
    with open(in_file, 'r', encoding='utf-8') as f:
        text = f.read()
        return len(text.split())

def get_verbs(nlp, doc_orig_name, doc_count):
    verbs = set()
    for i in range(0, doc_count):
        print(f'processing {i}...')
        
        doc_name = f'{doc_orig_name.split('.')[0]}{i}{doc_orig_name.split('.')[1]}'
        doc = load_doc(doc_name, nlp)
        
        for token in doc:
            if token.pos_ == 'VERB':
                verbs.add(token.text)
                
        print(f'done processing {i}')
    return verbs

def chunk_text(text, chunk_size):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def chunks_to_docs(text, chunk_size, nlp):
    chunks = chunk_text(text, chunk_size)
    
    for i, chunk in enumerate(chunks):
        print(f'converting to doc {i}...')
        doc = nlp(chunk)
        print(f'done converting to doc {i}')

        print(f'saving to disk {i}...')
        save_doc_to_disk(doc, f'doc_all{i}.spacy')
        print(f'done saving to disk {1}')