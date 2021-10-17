import speech_recognition as sr
import pyaudio

recog = sr.Recognizer()

finalText = []

for i in range(1, 6):
    filename = "part" + str(i) + ".wav"
    print(filename)

    with sr.AudioFile(filename) as source:
        print('Audio analysed')
        recog.adjust_for_ambient_noise(source)
        audio = recog.record(source)

    try:
        text = recog.recognize_google(audio)
        finalText.append(text)
        print(text)

    except Exception as e:
        print(e)

listText = ' '.join(finalText)
print(listText)