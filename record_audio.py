import speech_recognition as sr

# Create a recognizer instance
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

# Save the recorded audio to a file (optional)
with open("recorded_audio.wav", "wb") as f:
    f.write(audio.get_wav_data())
