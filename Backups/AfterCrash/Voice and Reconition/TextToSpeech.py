import gtts
import os
from playsound import playsound

def talkBack(text):
    tts = gtts.gTTS(text)
    tts.save("responseMessage.mp3")
    playsound("responseMessage.mp3")

    #has to delet or it will error out
    if os.path.exists("responseMessage.mp3"):
      os.remove("responseMessage.mp3")
    else:
      print("The file does not exist")
