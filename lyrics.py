import time
import threading
import sys

# Create a lock for thread safety
lock = threading.Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # Add newline after each lyric line

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("I DON'T MIND SPENDING EVERY DAY", 0.1),
        ("OUT ON YOUR CORNER IN THE POURING RAIN", 0.1),
        ("LOOK FOR THE GIRL WITH THE BROKEN SMILE", 0.1),
        ("ASK HER IF SHE WANTS TO STAY A WHILE?", 0.1),
        ("AND SHE WILL BE LOVED", 0.1),
        ("AND SHE WILL BE LOVED", 0.1),
        ("AND SHE WILL BE LOVED", 0.1),
        ("AND SHE WILL BE LOVED", 0.1)
    ]

    delays = [0.2, 4.5, 8.8, 15.0, 17.0, 23.0, 29.0, 32.0]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = threading.Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    # Optional: wait for all threads to finish
    for t in threads:
        t.join()

sing_song()

