import pyttsx3

engine = pyttsx3.init()
remainder = input("Enter your reminder: ")
engine.say(remainder)
engine.runAndWait()

print(f"spoken: {remainder}")