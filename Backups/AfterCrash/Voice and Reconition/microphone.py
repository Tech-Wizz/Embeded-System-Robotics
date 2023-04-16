#STARTER CODE GIVEN
import speech_recognition as sr

listening = True

while listening:
    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)
        r.dyanmic_energythreshhold = 3000

        try:
            print("listening")
            audio  = r.listening(source)
            print("Got audio")
            word = r.reconize_google(audio)
            print(word)
        except sr.UnknownValueError:
            print("Don't  know that word")

#mic = sr.Microphone()

#with mic as source:
#        au = r.listen(source)

#print("here")
#word = r.reconize_google(au)
#print("here" word)
