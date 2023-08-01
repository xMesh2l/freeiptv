#! /usr/bin/python3

import requests
import os
import sys

print('#EXTM3U')
print('#EXT-X-VERSION:5')
print('#EXT-X-STREAM-INF:BANDWIDTH=3032655,AVERAGE-BANDWIDTH=2756959,CODECS="avc1.64001f,mp4a.40.2",RESOLUTION=1280x720,FRAME-RATE=25.000,AUDIO="audio-AACL-96",SUBTITLES="text"')
s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://simulcast-p.ftven.fr/simulcast/France_5/hls_fr5/index.m3u8')
#print(response.text)

string = response.text
new_string = string.replace("index", "France_5-avc1_2500000=10001")
print(new_string)
new2_string = string.replace("index", "France_5-mp4a_96000_fra=20000")
print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-AACL-96",LANGUAGE="fr",NAME="Francais",DEFAULT=YES,AUTOSELECT=YES,CHANNELS="2",URI="{new2_string}"')

if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
