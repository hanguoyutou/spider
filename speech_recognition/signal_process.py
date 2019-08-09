import numpy as np
from matplotlib import pyplot as plt
import speech_recognition as sr
from scipy.io import wavfile

recording = sr.Recognizer()

with sr.Microphone() as source:
    recording.adjust_for_ambient_noise(source)
    print('say something...')
    audio = recording.listen(source,5)

frequency_sampling, audio_signal = wavfile.read(audio)
