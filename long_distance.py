import pygame
import time
from colorama import Fore, Style, init

# Initialize colorama (for Windows color support)
init(autoreset=True)

# Initialize the mixer
pygame.mixer.init()
pygame.mixer.music.load("ldcut.mp3")  # make sure the file is in the same folder
pygame.mixer.music.play()

# Lyrics with timing (line, delay in seconds)
lyrics = [
    ("যদি বিরহ থাকে আমিও থাকি", 3),
    ("কে বলো শেষ হবে আগে?", 3),
    ("কেন যে এত ভালোবাসা মরে যায়", 3),
    ("শুধু সময় মনে রাখে", 3)
    ("এত শূন্যতা এ মনে রাখি যে আমি", 3),
    ("দেখে না কেউ তো আর, বলে এ সবই পাগলামি", 3),
    ("কাটে না যামিনী, বিরহ যেন কেটে যায়", 3),
    ("থামে না বরষা, তোমারে ডাকি যে আমি", 3)
    ("আর", 3),
    ("সে থাকে কার ভরসায়?", 3),
      
]

# Show lyrics like subtitles
for line, delay in lyrics:
    print(Fore.YELLOW + Style.BRIGHT + line)
    time.sleep(delay)

# Wait until song finishes
while pygame.mixer.music.get_busy():
    time.sleep(1)

print(Fore.CYAN + "\n🎵 Song finished 🎵")
