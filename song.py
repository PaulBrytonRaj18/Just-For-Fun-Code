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

"""
Dustin:
Turn around
Look at what you see
In her face
The mirror of your dreams

Dustin and Suzie:
Make believe I'm everywhere
Given in the light
Written on the pages
Is the answer to a never ending story
Ah


Reach the stars
Fly a fantasy
Dream a dream
And what you see will beRhymes that keep their secrets
Will unfold behind the clouds
And there upon a rainbow
Is the answer to a never ending story
Ah
Story
Ah


Show no fear
For she may fade away
In your hand
The birth of a new dayRhymes that keep their secrets
Will unfold behind the clouds
And there upon a rainbow
Is the answer to a never ending story
Ah
Never ending story
Ah
Never ending story
Ah
Never ending story
Ah
    """