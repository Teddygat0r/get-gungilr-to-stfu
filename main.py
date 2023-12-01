import pyaudio
import numpy as np

# Constants for the audio stream
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Number of frames per buffer

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open a stream to capture audio from the microphone
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Listening...")

try:
    while True:
        # Read audio data from the stream
        data = stream.read(CHUNK)
        
        # Convert the data to an array of integers
        audio_data = np.frombuffer(data, dtype=np.int16)
        
        # Calculate the root mean square (RMS) to estimate the volume
        rms = np.sqrt(np.mean(np.square(audio_data)))
        
        # Print the volume (RMS value)
        print(f"Volume: {rms}")

except KeyboardInterrupt:
    pass

finally:
    # Close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("Stream closed. Exiting.")