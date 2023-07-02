import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

fs = 44100  # Sample rate
seconds = 520  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
print("Recording Audio")
sd.wait()  # Wait until recording is finished
print("Audio recording complete , Play Audio")
sd.play(myrecording, fs)  # Play the recorded sound back
sd.wait()
print("Play Audio Complete")

# Save as WAV file
wav.write('my_recording.wav', fs, myrecording)
