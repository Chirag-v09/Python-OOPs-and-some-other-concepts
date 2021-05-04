
import winsound
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)


# On Linux and Mac
import os
duration = 1  # seconds
freq = 440  # Hz
os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))


# On Debian / Ubuntu / Linux Mint, run this in your terminal:
'''sudo apt install sox'''


# On Mac, run this in your terminal (using macports):
import os
os.system('say "your program has finished"')


# Speech on Linux
import os
os.system('spd-say "your program has finished"')
# You need to install the speech-dispatcher package in Ubuntu
# (or the corresponding package on other distributions):
'''sudo apt install speech-dispatcher'''

