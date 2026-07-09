from gtts import gTTS

tts = gTTS("Hello Abhishek, VS Code is now using the right environment!", lang="en")
tts.save("test.mp3")
print("MP3 created successfully!")
