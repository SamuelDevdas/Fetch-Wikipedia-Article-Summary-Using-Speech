## Search for existing 'Wikipedia Article Summaries', e.g. "Michael Jordan", "Pycharm", "Donald trump" etc. using 'Speech Recognition'. Hear back the result: 'Page summary' as 'Human Voice'.

### Description
This script allows the user to perform a voice search on Wikipedia using the SpeechRecognition and Pyttsx3 libraries in Python. The script records the user's voice input through the computer's microphone, converts it to text using the Google Speech Recognition API, and passes the text as a search query to the Wikipedia API. The script then retrieves the summary of the Wikipedia article related to the search query and reads it out loud using the text-to-speech functionality provided by Pyttsx3.

### Requirements
In order to run this script, you will need to have Python 3 installed on your computer. You will also need to install the following external libraries using pip:

pyttsx3
speech_recognition
wikipedia
Additionally, you will need an active internet connection to access Wikipedia.

### Usage
- Open the script in your preferred Python environment.
- Run the script.
- When prompted by the "Speech bot1" instance, speak your search query into the microphone.
- The script will then search Wikipedia for the article related to the query and retrieve the summary.
- The summary will be read out loud by the "bot2" instance.

### Note
- If the speech recognition functionality does not work properly, you can try adjusting the microphone sensitivity or the microphone's position.
- The script retrieves the summary of the first Wikipedia article that matches the search query. If you want to retrieve the summary of a specific article, you can modify the script to include the article's title in the search query.

- Difficult or unclear pronunciations might cause an error, therefore, use slow and clear speech.
- Check using the Wikipedia 'Search bar', if the 'search query' gives a direct 'Wikipedia article page', not a list of results. The 'wikipedia.page()' method functions like the Wikipedia 'Search bar'.  
