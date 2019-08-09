import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.silence import detect_silence
import os
from time import time

# transform time form
def transform_time(t):
    t, ms = divmod(t,1000)
    t, s = divmod(t,60)
    h, m = divmod(t, 60)
    ms = str(ms)
    s = str(s)
    m = str(m)
    h = str(h)
    while len(ms) < 3:
        ms = '0' + ms
    while len(s) < 2:
        s = '0' + s
    while len(m) < 2:
        m = '0' + m
    while len(h) < 2:
        h = '0' + h
    return h+':'+m+':'+s+','+ms

def silence_based_conversation():
    name_list = ['banwo01','dushen1','dushen2','shuangxiong','wushuang','yidanhongchun']
    name = name_list[0]
    path = name + '.mp3'
    song = AudioSegment.from_mp3(path)
    fh = open(name + ".srt", "w+")

    min_silence_len=530
    silence_thresh=-35
    keep_silence=1000

    chunks = split_on_silence(song,
                              min_silence_len=min_silence_len,
                              silence_thresh=silence_thresh,
                              keep_silence=keep_silence
                              )
    silences = detect_silence(song,
                              min_silence_len=min_silence_len,
                              silence_thresh=silence_thresh
                              )

    try:
        os.mkdir('segment'+'_'+name)
    except(FileExistsError):
        pass

    os.chdir('segment'+'_'+name)
    for i,chunk in enumerate(chunks):
        chunk_silent = AudioSegment.silent(duration=500)
        audio_chunk = chunk_silent + chunk + chunk_silent
        print('saving chunk{0}.wav'.format(i))
        audio_chunk.export("./chunk{0}.wav".format(i), format='wav')
        filename = 'chunk'+str(i)+'.wav'
        print("Processing chunk "+str(i))

        file = filename

        r = sr.Recognizer()

        with sr.AudioFile(file) as source:
            r.adjust_for_ambient_noise(source)
            audio_listened = r.listen(source)

        try:
            rec = r.recognize_google(audio_listened,language='zh-yue')
            fh.write('{0}\n'.format(i+1))
            fh.write(transform_time(silences[i][1])+' --> '+transform_time(silences[i+1][0])+'\n')
            fh.write(rec+'\n')
            fh.write('\n')
        except sr.UnknownValueError:
            fh.write('{0}\n'.format(i + 1))
            fh.write(transform_time(silences[i][1]) + ' --> ' + transform_time(silences[i + 1][0]) + '\n')
            fh.write('Could not understand audio.' + '\n')
            fh.write('\n')
            print('Could not understand audio.')
        except sr.RequestError:
            print("Request errors happened.")
    fh.close()
    os.chdir('..')

if __name__ == '__main__':
    start = time()
    silence_based_conversation()
    end = time()
    print("total running time:",end-start)