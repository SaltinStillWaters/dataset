import re
import os
import yt_dlp
from pytube import Playlist
from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path
import spacy
from spacy.tokens import Doc

# SPACY
def save_doc_to_disk(doc, out_file):
    doc.to_disk(Path(out_file))

def load_doc(in_file, nlp):
    return Doc(nlp.vocab).from_disk(in_file)


# GENERAL
def chunk_text(text, chunk_size=400000):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def concatenate_transcripts(out_name, transcript_name='raw_transcripts'):
    transcript_path = Path(transcript_name)
    
    with open(out_name, 'w', encoding='utf-8') as out_file:
        for file in transcript_path.rglob('*.txt'):
            print(f'adding file: {file}...')
            with open(file, 'r', encoding='utf-8') as in_file:
                out_file.write(in_file.read() + '\n')
    
def get_playlist_transcripts(playlist_url, out_file):
    playlist = Playlist(playlist_url)
    video_urls = playlist.video_urls
    
    with open(out_file, 'a', encoding='utf-8') as f:
        for url in video_urls:
            video_id = url.split('v=')[-1]
            ydl_opts = {'quiet': True, 'extract_flat': True}
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                video_title = info.get('title', 'No title found')
            
            f.write(f"Transcript for: {video_title}\n")
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                for entry in transcript:
                    f.write(entry['text'] + ' ')
            except Exception as e:
                f.write(f'Could not get transcript of {video_title}: {e}')
                print(f'Could not get transcript of {video_title}: {e}')
            finally:
                f.write('\n\n')
def split_transcripts(input_file, output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    dir_name = os.path.basename(os.path.normpath(output_dir))

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    transcripts = re.split(r'Transcript for:\s*', content)

    for i, transcript in enumerate(transcripts[1:], start=1):
        if not transcript.strip():
            continue

        lines = transcript.split('\n')
        title = lines[0].strip()
        transcript_content = '\n'.join(lines[1:]).strip()

        full_content = f"Transcript for: {title}\n{transcript_content}"

        filename = f"{dir_name}-{i}.txt"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"Created: {filepath}")

def clean_transcripts(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            parts = content.strip().split('. ')
            sentences = [part.strip() + '.' for part in parts if part]

            if content.strip().endswith('.'):
                sentences[-1] = sentences[-1][:-1]  

            cleaned_content = '\n'.join(sentences)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)

            print(f"Cleaned: {filepath}")

