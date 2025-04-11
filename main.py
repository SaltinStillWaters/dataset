import utils
from pathlib import Path

utils.get_playlist_transcripts('https://youtube.com/playlist?list=PLJXAX8ka78LQ430gnvSbC52qW7TVMwANE&si=N2Fq3-nxvqaRQqAP', 'freecodecamp.txt')
utils.split_transcripts('FreeCodeCamp.txt', r'raw_transcripts\freecodecamp')