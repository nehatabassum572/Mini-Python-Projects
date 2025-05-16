from playsound import playsound 
import time 

CLEAR="\033[2J" #clears the terminal so only alarm stuff will be shown
CLEAR_AND_RETURN="\033[H" #overwrites on the same line itself

def alarm(seconds):
    time_elapsed=0 #tells us how time has passed
    
    print(CLEAR)
    while time_elapsed < seconds: #goes on till the time left is = to user input 
        time.sleep(1) # we are gonna pause the time a little bit else the comp will rush not stop for milliseconds n all
        time_elapsed += 1 #increment it by 1
        
        time_left= seconds-time_elapsed #gives us how much time is left i.e, total time - how much time passes 
        minutes_left= time_left // 60 # u r dividing the time left with 60, to get the int part of decimal 
        sec_left= time_left % 60 # ur finding modulo to get the part after '.' of decimal 
        
        print(f"{CLEAR_AND_RETURN}Alarm will sound in:{minutes_left:02d}:{sec_left:02d}")
        
    
    print("\n Time's up! Playing alarm...")
    playsound(r"C:\\Users\\hp\\Music\\alarm_sound.mp3")
    
minutes=int(input("How many minutes to wait:"))
seconds=int(input("How many seconds to wait:"))
total_seconds= minutes * 60 + seconds #converts the min into seconds & adds the seconds also
alarm(total_seconds)