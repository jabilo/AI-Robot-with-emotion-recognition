from flask import Flask, render_template,redirect,url_for
import subprocess
import play_rhymes
import play_stories
import time


face_emotion_id = 1

app = Flask(__name__)

@app.route('/')
def home():
    if face_emotion_id == 0:
        video_file = "happy.mp4"
    elif face_emotion_id == 1:
        video_file = "cute.mp4"
    elif face_emotion_id == 3:
        video_file = "sad.mp4"
    else:
        video_file = "mad.mp4"
    return render_template('index.html',video_file = video_file)

@app.route('/chat')
def button1():
    subprocess.run(['python', 'bunny_updated_v2.py'])
    return 'File 1 executed'

@app.route('/play_rhyme')
def button2():
    # subprocess.run(['python', 'play_rhymes_fun_call.py'])
    play_rhymes.play_rhyme()
    return 'File 2 executed'

@app.route('/stop_rhyme')
def button3():
    # subprocess.run(['python', 'play_rhymes_fun_call.py'])
    play_rhymes.stop_rhyme()
    return redirect(url_for('home'))

@app.route('/play_story')
def button4():
    # subprocess.run(['python', 'play_stories_fun_call.py'])
    play_stories.play_story()
    return 'File 3 executed'

@app.route('/stop_story')
def button5():
    # subprocess.run(['python', 'play_rhymes_fun_call.py'])
    play_stories.stop_story()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
