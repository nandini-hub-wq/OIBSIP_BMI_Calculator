import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    speak("Hello, how can I help you today?")
    while True:
        query = take_command().lower()

        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'stop' in query:
            speak("Goodbye!")
            break
