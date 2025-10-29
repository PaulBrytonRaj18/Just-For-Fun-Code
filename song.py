import time
import sys

def song_play():
    lyrics = [
        "\n\nRun Odu Naa Win Avena",
        "Unnodu Nan Onnavena",
        "Nee Illana Ennaaven Naa",
        "Gundae Illa Gun Avena\n",
        "Freetime La God Oda Naan",
        "Pottu Vechen Deal Onnu Ma",
        "Yenna Nu Than Nee Kelu Ma",
        "Ennaikum Nee En Aalu Ma",
        "..........",
        "..........",
        "Fun_Code by Paul Bryton Raj"
    ]

    delay = [0.1, 0.5, 0.5, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]  # Delays for each verse
    time.sleep(1)  # Initial delay before starting the song
    
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)  # Typing effect
        print()  # New line after each verse
        time.sleep(delay[i])  # Pause for the specified delay between verses
    time.sleep(1)  # Final pause before ending
    
if __name__ == "__main__":
    song_play()