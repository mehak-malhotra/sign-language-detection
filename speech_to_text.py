import whisper  
import pyaudio  
import wave  
import torch  
import warnings  

def stt():
    # Whisper model load karo (Bigger model better hai names ke liye)
    model = whisper.load_model("base").to("cpu")

    # FP32 enforce karne ke liye model ko manually convert karo
    for m in model.modules():
        if isinstance(m, torch.nn.Linear) or isinstance(m, torch.nn.Conv1d):
            m.float()

    # Whisper warnings ignore karne ke liye
    warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

    # Audio recording settings  
    FORMAT = pyaudio.paInt16  
    CHANNELS = 1  
    RATE = 44100  
    CHUNK = 1024  
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "live_audio.wav"  

    # PyAudio object banayein  
    audio = pyaudio.PyAudio()  

    # Audio stream start karo  
    stream = audio.open(format=FORMAT, channels=CHANNELS,  
                        rate=RATE, input=True,  
                        frames_per_buffer=CHUNK)  

    print("🎤 Speak Now... (Recording)")  
    frames = []  

    # Audio record karna  
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):  
        data = stream.read(CHUNK)  
        frames.append(data)  

    print("✅ Recording Done, Transcribing...")  

    # Stream stop aur close karo  
    stream.stop_stream()  
    stream.close()  
    audio.terminate()  

    # Audio ko WAV file me save karo  
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')  
    wf.setnchannels(CHANNELS)  
    wf.setsampwidth(audio.get_sample_size(FORMAT))  
    wf.setframerate(RATE)  
    wf.writeframes(b''.join(frames))  
    wf.close()  

    # Improved transcription for better name recognition  
    result = model.transcribe(
        WAVE_OUTPUT_FILENAME,  
        language="hi",      # Hindi bias rakhne ke liye  
        temperature=0,      # Confident prediction ke liye  
        beam_size=5,        # Better word detection  
        fp16=False          # FP32 force karne ke liye  
    )

    # Output print karo  
    text =  result["text"]
    return text