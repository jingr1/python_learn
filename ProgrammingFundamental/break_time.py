import time
import webbrowser
total_breaks = 3
break_count = 0
print("This program start on "+time.ctime())
while(break_count <total_breaks):
    time.sleep(10)
    webbrowser.open("http://v.youku.com/v_show/id_XMzAzNzAwODg1Ng==.html?spm=a2h1n.8251843.0.0&f=26079431")
    break_count = break_count + 1
    
