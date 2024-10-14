import moviepy
from moviepy.editor import *
from moviepy.editor import VideoFileClip

clip = VideoFileClip("assets/intro.mp4")
# 848x384
c = clip.crop(x1=70, y1=0, x2=848-70, y2=384)
c.write_videofile("cropped.mp4")