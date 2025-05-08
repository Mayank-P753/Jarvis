import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import schedule
import time

# Initialize voice engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# Task list
tasks = []

# Speak function
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print(f"User said: {command}")
        except:
            command = ""
        return command

# Handle commands
def run_jarvis():
    command = listen()

    if "time" in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"Current time is {current_time}")

    elif "date" in command:
        today = datetime.date.today()
        talk(f"Today's date is {today}")

    elif "play" in command:
        song = command.replace('play', '')
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "add task" in command:
        task = command.replace('add task', '').strip()
        tasks.append(task)
        talk(f"Task '{task}' added.")

    elif "show tasks" in command:
        if tasks:
            talk("Your tasks are:")
            for task in tasks:
                talk(task)
        else:
            talk("You have no tasks.")

    elif "remind me" in command:
        remind_text = command.replace('remind me', '').strip()
        schedule.every(10).seconds.do(reminder, remind_text=remind_text)  # every 10 sec for testing
        talk(f"I will remind you to {remind_text}")

    elif "exit" in command:
        talk("Goodbye!")
        exit()

    else:
        talk("Please say the command again.")

# Reminder function
def reminder(remind_text):
    talk(f"Reminder: {remind_text}")
    return schedule.CancelJob

# Main loop
talk("Hello, I am Jarvis. How can I help you today?")
while True:
    run_jarvis()
    schedule.run_pending()
