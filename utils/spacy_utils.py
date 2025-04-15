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

def get_verbs(nlp, doc_orig_name, doc_count, container):
    verbs = container
    for i in range(0, doc_count):
        print(f'processing {i}...')
        
        doc_name = f'{doc_orig_name.split('.')[0]}{i}.{doc_orig_name.split('.')[1]}'
        doc = load_doc(doc_name, nlp)
        
        for token in doc:
            if token.pos_ == 'VERB':
                if isinstance(verbs, set):
                    verbs.add(token.lemma_)
                elif isinstance(verbs, list):
                    verbs.append(token.text)
        print(f'done processing {i}')
    return verbs

def get_keywords(nlp, text_orig_name, text_count, container, keywords):
    string = ''
    for i in range(0, text_count):
        verbs = type(container)()
        text_name = f'{text_orig_name.split('.')[0]}{i}.{text_orig_name.split('.')[1]}'
        text = read_file(text_name)
        doc = nlp(text)
        
        for token in doc:
            if token.lemma_.lower() in keywords:
                if isinstance(verbs, set):
                    verbs.add(token.lemma_)
                elif isinstance(verbs, list):
                    verbs.append(token.text)
        string += f'#{i+2}: {len(verbs)}'
        print(f'{i}/{text_count-1}')
    return string

def get_verbs_from_text(nlp, text_orig_name, text_count):
    string = ''
    for i in range(0, text_count):
        verbs = set()
        text_name = f'{text_orig_name.split('.')[0]}{i}.{text_orig_name.split('.')[1]}'
        try:
            text = read_file(text_name)
        except:
            print(f'skipping {i}...')
            continue
        doc = nlp(text)
        
        title = text.split('\n')[0]
        string += f'#{i}: {title}\n\n'
        for token in doc:
            if token.pos_ == 'VERB':
                verbs.add(token.text)
        string += f'{verbs}\n\n\n'
    return string

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