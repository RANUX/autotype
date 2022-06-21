import pyaudio
import wave
import time

# Set chunk size of 1024 samples per data frame
CHUNK_SIZE = 1024

# play a wav file
def play_wav(wav_file):
    wf = wave.open(wav_file, 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)
    
    # Read data in chunks
    data = wf.readframes(CHUNK_SIZE)

    # Play the sound by writing the audio data to the stream
    while data:
        stream.write(data)
        data = wf.readframes(CHUNK_SIZE)
    time.sleep(0.5)

    # Close and terminate the stream
    stream.close()
    p.terminate()


if __name__ == '__main__':
    play_wav('audio/block_1.wav')