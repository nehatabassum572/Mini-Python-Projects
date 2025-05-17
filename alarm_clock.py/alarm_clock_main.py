from playsound import playsound 
import time 

def alarm(seconds):
    time_elapsed = 0
    
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        sec_left = time_left % 60
        
        # Use \r to overwrite the same line
        print(f"\rAlarm will sound in: {minutes_left:02d}:{sec_left:02d}", end='', flush=True)
    
    # Move to a new line and show final message
    print("Time's up! Playing alarm...")
    try:
        playsound(r"C:\Users\hp\Music\alarm_sound.mp3")  # Verify path
    except Exception as e:
        print(f"Error playing sound: {e}")

# Get user input
try:
    minutes = int(input("How many minutes to wait: "))
    seconds = int(input("How many seconds to wait: "))
    total_seconds = minutes * 60 + seconds
    alarm(total_seconds)
except ValueError:
    print("Please enter valid numbers for minutes and seconds.")