import pyttsx3
import speech_recognition as sr
import wikipedia

# Create Speech recognition instance
recognizer = sr.Recognizer()

# Use .microphone method to instantiate the mic for voice inputs
# Create a 'text to speech' instance for a 'Speech bot1' which asks the user to utter a search query
with sr.Microphone() as mic:
    bot1 = pyttsx3.init()
    print('Speak now.....')
    bot1.say('Speak now')  # Speech bot1: The user hears "Speak now" as an instruction
    bot1.runAndWait()
    # recogniser listens to the source: mic audio by the .listen method
    user_query = recognizer.listen(mic)
    # The audio 'user_query' audio gets recognized as text by the .recognize_google method
    text = recognizer.recognize_google(user_query)
    print(text)

# The voice query converted as text passed into the .page method
article = wikipedia.page(text)
print(article.summary[:500])  # using only the first 500 characters of the summary
page_summary = article.summary[:500]

# The article summary generated is voice outputted by 'bot2'
bot2 = pyttsx3.init()
bot2.say(page_summary)
bot2.runAndWait()
