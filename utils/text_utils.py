import re
import yt_dlp
import os
from bisect import bisect_right
from pytube import Playlist
from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path

# GENERAL
def chunk_text(text, chunk_size=400000):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(data, out_file, open_mode='w', delim=' '):
    if isinstance(data, list):
        data = delim.join(data)
    elif isinstance(data, str):
        pass
    else:
        print(f'invalid data: {data}')
        return
    
    with open(out_file, open_mode, encoding='utf-8') as f:
        f.write(data)

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
        
        text = re.sub(r'\n', ' ', text)
        text = re.sub(r' *\.', '.', text)
        text = re.sub(r'\. *', '.\n', text)
        text = re.sub(r'\? *', '?\n', text)
        text = re.sub(r', *', ', ', text)
        text = re.sub(r'  +', ' ', text)

        write_file(text, file_name)
        
def concatenate_transcripts(out_name, transcript_name='raw_transcripts'):
    transcript_path = Path(transcript_name)
    
    with open(out_name, 'w', encoding='utf-8') as out_file:
        for file in transcript_path.rglob('*.txt'):
            print(f'adding file: {file}...')
            with open(file, 'r', encoding='utf-8') as in_file:
                out_file.write(in_file.read() + '\n')

def split_chapters(in_file, out_dir):
    text = read_file(in_file)
    
    vid_title = text.split('\n')[0]
    vid_title = vid_title.split('Transcript for:')[1].strip()
    
    out_dir += vid_title + '/'
    print(out_dir)
    
    os.makedirs(out_dir, exist_ok=True)
    
    for i, chap in enumerate(text.split('### ')[1:]):
        lines = chap.split('\n')
        title = lines[0] + '.'
        content = '\n'.join(lines[1:]).strip()
        
        print(title)
        if not content:
            print(f'{title} is empty. Skipping...')
            continue
        
        write_file(title + content, f'{out_dir}{i}.txt')
        count = i
    
    clean_text(f'{out_dir}.txt', count)
    
def get_chaptered_transcript(video_url, languages=['en', 'en-US'], out_dir=''):
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(video_url, download=False)
        video_id = info['id']
        video_title = info.get('title', 'Untitled')
        chapters = info.get('chapters', [])

    out_file = f'{out_dir}{video_title}'
    
    if not chapters:
        print("No chapters found in the video.")
        return

    for language in languages:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
            break
        except Exception as e:
            print(f"Could not get transcript: {e} lang: {language}")
    else:
        return
    
    chapter_starts = [ch['start_time'] for ch in chapters]
    chapter_titles = [ch['title'] for ch in chapters]
    grouped_transcript = {title: [] for title in chapter_titles}

    for entry in transcript:
        idx = bisect_right(chapter_starts, entry['start']) - 1
        chapter_title = chapter_titles[max(idx, 0)]
        grouped_transcript[chapter_title].append(entry['text'])

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(f"Transcript for: {video_title}\n\n")
        for title, texts in grouped_transcript.items():
            f.write(f"### {title}\n")
            f.write(' '.join(texts) + '\n\n')

    print(f"Transcript written to {out_file}")

    
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
                transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en-US'])
                for entry in transcript:
                    f.write(entry['text'] + ' ')
            except Exception as e:
                f.write(f'Could not get transcript of {video_title}: {e}')
                print(f'Could not get transcript of {video_title}: {e}')
            finally:
                f.write('\n\n')