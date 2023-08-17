import speech_recognition as sr
import math
import time
import serial
# from espeak import espeak
import sys
import openai
import subprocess
from gtts import gTTS
from datetime import datetime
import pyttsx3

import random
import pyaudio
import wave
import play_rhymes
import play_stories
 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
CHUNK = 512
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "voice.wav"
device_index = 1
audio = pyaudio.PyAudio()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# pygame.mixer.init()
model_to_use="text-davinci-003" # most capable
#model_to_use=”text-curie-001”
#model_to_use=”text-babbage-001”
#model_to_use="text-ada-001" # lowest token cost

r = sr.Recognizer()
openai.api_key="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"
def chatGPT(query):
    response = openai. Completion.create(
    model=model_to_use,
    prompt=query,
    temperature=0,
    max_tokens=1000
    )
    return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']
def main():
    print('LED is ON while button is pressed (Ctrl-C for exit).')
    
    while True:
        print("inside while loop....")
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 48000
        CHUNK = 512
        
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "voice.wav"
        device_index = 1
        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,input_device_index = device_index,
                frames_per_buffer=CHUNK)
        print ("recording started")
        Recordframes = []
        print(audio)                                                                                                                                                        
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            Recordframes.append(data)
           
        print ("recording stopped")
                 
        stream.stop_stream()
        stream.close()
        audio.terminate()
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(Recordframes))
        waveFile.close()
                    
          
        
        print("Recognizing Now....")
        try:
            print('inside try')
            with sr.AudioFile("voice.wav") as source:
                audio_data = r.record(source)
                
            command=str(r.recognize_google(audio_data))
            print(command)
            if(("rhyme" or "rhymes" or "music") in command):
                    print(command)
                    print("playing rhymes")
                    speak("playing rhymes, have fun")
                    play_rhymes.play_rhyme()
            elif(("story" or "stories" ) in command):
                    print(command)
                    print("ok let me tell you a story")
                    speak("playing rhymes, have fun")
                    play_stories.play_story()
            elif(("fuck" or "shit" or "crap") in command):
                speak("sootha moodra sunni !!")
                break
            else:
                print("Google Speech Recognition thinks you said", command)
                query=command
                (res, usage) = chatGPT(query)
                print(res)
                speak(res)
                print("done speaking")
                main()
        except:
            print("no audio")
            main()
        
        # tts = gTTS(text=res, lang='en')
        # date_string = datetime.now().strftime("%d%m%Y%H%M%S")
        # filename = "voice"+date_string+".mp3"
        # tts.save("voice.mp3")
        # pygame.mixer.music.load("voice.mp3")
        # pygame.mixer.music.play()
        
#espeak.synth(res)
 
if __name__ == '__main__':
    main()
