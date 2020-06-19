import pyttsx3

msg = '''I love you three thousand'''
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 100)
engine.say(msg)
engine.runAndWait()
