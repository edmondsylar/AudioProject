import wave
import pyaudio
import keyboard

CHUNK = 1024 
FORMAT = pyaudio.paInt16 # 16-bit int sampling
CHANNELS = 1 # mono
RATE = 44100 # 44.1 kHz sampling rate


while True:
    p = pyaudio.PyAudio()

    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

# request user for input
    RecordingName = input("Enter Recording Name: ")
    if RecordingName:
        # os.sys("cls")
        print("Recording...")

        frames = []

        # Loop forever until 'S' pressed
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
            if keyboard.is_pressed('S'):
                break
            

        print("Recording stopped.")

        # Clean up
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Save audio file
        wf = wave.open(f"{RecordingName}.wav", 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        continue
    