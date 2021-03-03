import speech_recognition as s
from textblob import TextBlob
import re

# Create a function to clean the text
def cleanTxt(text):
 text = re.sub('@[A-Za-z0–9]+', '', text)  # Removing @mentions
 text = re.sub('https?:\/\/\S+', '', text)  # Removing hyperlink
 return text

# Create a function to get the subjectivity
def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity

# Create a function to get the polarity
def getPolarity(text):
   return  TextBlob(text).sentiment.polarity

# Create a function to compute negative (-1), neutral (0) and positive (+1) analysis
def getAnalysis(score):
 if score < 0:
  return 'Negative'
 elif score == 0:
  return 'Neutral'
 else:
  return 'Positive'

#create a object of Recognizer
sr=s.Recognizer()
print("I am your code and listening to you...........................")
with s.Microphone() as m:
 audio=sr.listen(m)
 query=sr.recognize_google(audio,language='eng-in')
 print(query)
 # Clean the text
 Text = cleanTxt(query)
 # Create two new variables 'Subjectivity' & 'Polarity'
 Subjectivity = getSubjectivity(Text)
 Polarity = getPolarity(Text)
 Analysis = getAnalysis(Polarity)
 # Show the result
 print('Subjectivity :' + str(Subjectivity))
 print('Polarity :' + str(Polarity))
 print ('Analysis :' + Analysis)











