import pyaudio
import numpy as np
import math
import struct

CHUNK = 1024

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=CHUNK)

print("Listening...")

def rms( data ):
    count = len(data)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, data )
    sum_squares = 0.0
    for sample in shorts:
        n = sample * (1.0/32768)
        sum_squares += n*n
    return math.sqrt( sum_squares / count )

try:
    while True:
        data = stream.read(CHUNK)
        rms = rms(data,2)
        print(rms)
       #print(f"Max: {np.max(audio_data)}, Min: {np.min(audio_data)}")
        
# Get gun to stfu by turning pc off
# Get gun to stfu by playing funny audio 
# Get gun to stfu by taking his discord auth token

except KeyboardInterrupt:
    pass