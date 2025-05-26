import pvporcupine
import pyaudio
import struct

def aguardar_palavra_chave(chave="jarvis"):
    porcupine = pvporcupine.create(keywords=[chave])
    pa = pyaudio.PyAudio()

    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Esperando por palavra-chave...")

    try:
        while True:
            audio = stream.read(porcupine.frame_length, exception_on_overflow=False)
            audio = struct.unpack_from("h" * porcupine.frame_length, audio)

            keyword_index = porcupine.process(audio)
            if keyword_index >= 0:
                print("Palavra-chave detectada!")
                break

    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()
