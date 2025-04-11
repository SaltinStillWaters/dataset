import yt_dlp
from pytube import Playlist
from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path

# GENERAL
def chunk_text(text, chunk_size=400000):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()
    
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