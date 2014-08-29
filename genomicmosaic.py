from bregman.suite import *
import os

# assumes a dir with WAV files at ~/mosaicdb
snd_dir = os.path.expanduser('~/dev/git/genomicmosaic/snd/')
audio_file = 'viola_1.wav'

x,sr,fmt = wavread(os.path.join(snd_dir, audio_file))

# no analysis or processing; just dump the audio to an output file

res = wavwrite(x, os.path.join(snd_dir, 'out.wav'), 44100)