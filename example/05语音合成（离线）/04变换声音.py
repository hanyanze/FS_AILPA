import pyttsx3

msg = '''I love you three thousand'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i in voices:
    engine.setProperty('voice', i.id)
    engine.say(msg)
engine.runAndWait()

