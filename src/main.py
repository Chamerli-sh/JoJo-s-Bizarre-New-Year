import window
import countdown
import time

running = True

while running:  
    window.showWindow(running)
    countdown.delta_time()
    window.showText(str(countdown.delta_time()))
    time.sleep(1)
    

