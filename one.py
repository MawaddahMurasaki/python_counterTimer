import time
import webbrowser


time.sleep(10)
webbrowser.open("https://www.youtube.com/watch?v=fKhdec3uyrQ")

total_breaks = 3
break_count = 0

while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=fKhdec3uyrQ")
    break_count = break_count + 1
