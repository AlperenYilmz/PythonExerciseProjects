from gtts import gTTS

text="uno dos tres, cinco sei site"

# text put and the lang selected must be in same language, duh.
# Also check gtts documents online for accents for en and es languages

processor=gTTS(text=text, tld="com.mx",lang="es", slow=True)

processor.save("C:/Users/alper/Documents/PycharmProjects/sample.mp3")