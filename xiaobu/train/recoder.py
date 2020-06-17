import os
import sys
import pyaudio
import wave,time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
TIME = 3

def rec(file_name, RECORD_SECONDS):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("开始录音......")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("录音结束\n")
    time.sleep(1)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


wavfile = sys.argv[1]
rec(wavfile, TIME)
 

