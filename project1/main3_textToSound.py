# 텍스트 음성 변환
from gtts import gTTS
from numpy import full_like
from playsound import playsound
text = " 안녕하세요. 파이썬 입니다."
tts = gTTS(text=text, lang='ko')
tts.save(r"project1\hi.mp3")
# playsound(r"project1\hi.mp3")


file_path = r'project1\textfortts.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()
tts = gTTS(text=read_file, lang='ko')
tts.save(r"project1\mytxt.mp3")
playsound(r"project1\mytxt.mp3")
