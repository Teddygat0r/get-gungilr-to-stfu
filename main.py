import pyaudio
import numpy as np

CHUNK = 1024

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=CHUNK)

print("Listening...")
try:
    while True:
        data = stream.read(CHUNK)
        
        audio_data = np.frombuffer(data, dtype=np.int16)
        print(audio_data)
       #print(f"Max: {np.max(audio_data)}, Min: {np.min(audio_data)}")
        
# Get gun to stfu by turning pc off
# Get gun to stfu by playing funny audio 
# Get gun to stfu by taking his discord auth token

except KeyboardInterrupt:
    pass