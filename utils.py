import yt_dlp
from pytube import Playlist
from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path

def get_playlist_transcripts(playlist_url, output_file):
    playlist = Playlist(playlist_url)
    video_urls = playlist.video_urls
    
    with open(output_file, 'a', encoding='utf-8') as f:
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