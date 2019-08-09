import speech_recognition as sr

recording = sr.Recognizer()

with sr.Microphone() as source:
    recording.adjust_for_ambient_noise(source)
    print('say something...')
    audio = recording.listen(source)
    # print(type(audio))
    # print(audio)

try:
    print('You said: \n' + recording.recognize_google(audio, language='zh-yue')) #for languge selection plz go to 'http://stackoverflow.com/a/14302134'
except Exception as e:
    print(e)