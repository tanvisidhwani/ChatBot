import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()
speaker = pyttsx3.init()

def set_reminder(task, time):
  
    print(f"Reminder set for {time}: {task}")

def create_todo(task):
    # Implement logic to add the task to a to-do list
    print(f"To-Do created: {task}")

def search_web(query):
    # Implement logic to search the web using the query
    print(f"Searching the web for: {query}")

def voice_assistant():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said: " + command)

        if "set a reminder" in command:
            # Extract the task and time from the command
            set_reminder("Complete the report", "tomorrow at 9:00 AM")
            speaker.say("Reminder set. Is there anything else I can help with?")
        elif "create a to-do" in command:
            # Extract the task from the command
            create_todo("Buy groceries")
            speaker.say("To-Do created. What else would you like to do?")
        elif "search the web" in command:
            # Extract the query from the command
            search_web("Python tutorials")
            speaker.say("Search completed. How else can I assist you?")

        speaker.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
    except sr.RequestError:
        print("Sorry, my speech service is currently unavailable.")

def main():
    while True:
        voice_assistant()

if __name__ == "__main__":
    main()
