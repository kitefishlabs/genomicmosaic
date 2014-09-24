from bregman.suite import *
import os

# assumes a dir with WAV files at ~/mosaicdb
snd_dir = os.path.expanduser('~/dev/git/public_projects/genomicmosaic/snd/')
audio_file = 'viola_1.wav'

x,sr,fmt = wavread(os.path.join(snd_dir, audio_file))



# perform analysis [see Note 1]

linfreqspeq = LinearFrequencySpectrum(x)
logfreqspeq = LogFrequencySpectrum(x)
melfreqspeq = MelFrequencySpectrum(x)
mfcc = MelFrequencyCepstrum
chroma = Chromagram(x)



dbpwr = dBPower(x)




# no analysis or processing; just dump the audio to an output file
# res = wavwrite(x, os.path.join(snd_dir, 'out.wav'), 44100)


 
 '''
 Note 1: These are the default params for the feature extractors:
default_feature_params()
{
    'sample_rate': 44100, # The audio sample rate
    'feature':'cqft',     # Which feature to extract (automatic for Features derived classes)
    'nbpo': 12,           # Number of Bands Per Octave for front-end filterbank
    'ncoef' : 10,         # Number of cepstral coefficients to use for cepstral features
    'lcoef' : 1,          # Starting cepstral coefficient
    'lo': 62.5,           # Lowest band edge frequency of filterbank
    'hi': 16000,          # Highest band edge frequency of filterbank
    'nfft': 16384,        # FFT length for filterbank
    'wfft': 8192,         # FFT signal window length
    'nhop': 4410,         # FFT hop size
    'window' : 'hamm',    # FFT window type 
    'log10': False,       # Whether to use log output
    'magnitude': True,    # Whether to use magnitude (False=power)
    'power_ext': ".power",# File extension for power files
    'intensify' : False,  # Whether to use critical band masking in chroma extraction
    'onsets' : False,     # Whether to use onset-synchronus features
    'verbosity' : 1       # How much to tell the user about extraction
}
'''