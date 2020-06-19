import pyttsx3

msg = '''盼望着，盼望着，东风来了，春天的脚步...'''
engine = pyttsx3.init()
engine.say(msg)
engine.runAndWait()
