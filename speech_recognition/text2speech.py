
from gtts import gTTS
import os

s = '大家好'
file = 'welcome.mp3'

tts = gTTS(s, lang='en-US',debug=True)

print(tts.LANGUAGES)

tts.save(file)

os.system('mpg123 '+file)