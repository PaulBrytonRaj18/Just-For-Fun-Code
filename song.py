import time
import sys

def type_out(text, speed=0.06):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def song_play():
    lyrics = [
        "They can say that I'm a Fool",
        "Still I’ll stand and smile so cool",
        "Love ah vida mudiyala da",
        "Heart oda switch um pudikala da\n",

        "Nee pesaatha na silent-a iruppen",
        "Nee pesina pothum naan life-a maruppen",
        "Yaaru enna sonnalum I'm your tool",
        "They can say anything… still I'm a fool for you.\n",

        "..........",
        "Fun_Code by Paul Bryton Raj"
    ]

    delays = [0.4] * len(lyrics)   # same delay for all, simple and clean

    time.sleep(0.5)
    for line, pause in zip(lyrics, delays):
        type_out(line)
        time.sleep(pause)

if __name__ == "__main__":
    song_play()
