import os
import sys
from time import sleep
import winsound

audio_path = "C:\\Users\\habib\\Downloads\\PIANOMAN.WAV.wav"

winsound.PlaySound(
    audio_path,
    winsound.SND_FILENAME | winsound.SND_ASYNC)

def waterfall(target, targetduration, rest, alphabet=".abcdefghijklmnopqrstuvwxyz '"):
    total_gap = sum(alphabet.index(char) for char in target)
    cur = ""
    for i in range(len(target)):
        for j in range(len(alphabet)):
            sys.stdout.write("\033[H\033[10A")
            char_to_show = alphabet[j]
            current_line = cur + char_to_show
            padding = (47 - len(current_line) // 2) * " "
            sys.stdout.write(f"{padding}{current_line}\033[K")
            sys.stdout.flush()
            if target[i] == alphabet[j]:
                cur += alphabet[j]
                break
            sleep(targetduration / total_gap)
    sleep(rest)

os.system('cls')
print("\n" * 30)
sys.stdout.write("\033[H\033[10A" + " " * 30 + "------PIANO MAN by Billy Joel-------")
sys.stdout.flush()
sleep(10.5)

lyrics = ["he said son can you play me a memory",
          "i'm not really sure how it goes",
          "but it's sad and it's sweet and i knew it complete",
          "when i wore a younger man's clothes",
          "la la la de de da",
          "la la de de da da da",
          "sing us a song you're the piano man",
          "sing us a song tonight",
          "well we're all in the mood for a melody",
          "and you've got us feeling alright.."]
duration = [2.5, 2.3, 2.6, 2.1, 2.6, 3.5, 2.5, 2.4, 2.6, 2.8]
for x in range (5):
    duration[x] = duration[x] + 0.5
rest =     [1, 1.5, 0.85, 1.8, 1.7, 3.6, 1.1, 1.25, 1, 0.4]

for i in range(len(lyrics)):
    waterfall(lyrics[i], duration[i], rest[i])
