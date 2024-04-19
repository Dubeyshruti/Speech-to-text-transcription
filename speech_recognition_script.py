import speech_recognition as sr

# Create a recognizer instance
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

try:
    # Recognize speech using Google Speech Recognition
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")
except sr.RequestError as e:
    print("Error fetching results from Google Speech Recognition service:", e)
