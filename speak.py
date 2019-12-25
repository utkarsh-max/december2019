from gtts import gTTS
from playsound import playsound
tts = gTTS('kya hal hi')
tts.save('speak.mp3')
playsound('speak.mp3')