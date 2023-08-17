import speech_recognition as sr
import os
import subprocess

# Set up the speech recognizer
r = sr.Recognizer()

# Define the words and their corresponding emotion videos
word_to_emotion = {
    'happy': 'happy.mp4',
    'sad': 'sad.mp4',
    'angry': 'mad.mp4',
    'cute': 'cute.mp4',
   
}

# Define the path to the directory containing the emotion videos
video_dir = 'D:\PROJECT_ROBOT\robo_expressions'

# Define the function to play the emotion video
def play_video(video_path):
    subprocess.call(['ffplay', '-nodisp', '-autoexit', video_path])

# Start the speech recognition loop
with sr.Microphone() as source:
    print("Speak the word to trigger an emotion video!")
    while True:
        try:
            # Listen for speech input
            audio = r.listen(source)

            # Recognize the speech input
            word = r.recognize_google(audio)

            # Check if the recognized word triggers an emotion video
            if word in word_to_emotion:
                # Construct the path to the emotion video
                video_path = os.path.join(video_dir, word_to_emotion[word])

                # Play the emotion video
                play_video(video_path)

        except sr.UnknownValueError:
            # Speech input was not recognized
            pass
