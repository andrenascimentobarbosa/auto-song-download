from moviepy.editor import VideoFileClip

file = "KASINO - Can´t Get Over (Clipe Oficial).mp4"

video = VideoFileClip(file)

audio = video.audio
file = file.replace(' ', '_')
file = file.replace("'", "")
file = file.lower()
audio.write_audiofile(file.replace('mp4', 'mp3'))

