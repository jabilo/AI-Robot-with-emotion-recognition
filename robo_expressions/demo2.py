from moviepy.editor import VideoFileClip

# Open the video file
clip = VideoFileClip('robo_expressions/sad.mp4')

# Play the video in a loop
while True:
    # Play the video from the beginning
    clip = clip.fx('loop', n=1)

    # Display the video
    clip.preview()

# Close the video window
clip.close()
