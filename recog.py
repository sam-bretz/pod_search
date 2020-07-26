import speech_recognition as sr


def transcribe(file):
  # Initialize recognizer class (for recognizing the speech)
  r = sr.Recognizer()

  # Reading Audio file as source
  # listening the audio file and store in audio_text variable

  with sr.AudioFile(file) as source:

      audio_text = r.listen(source)

  # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

      # using google speech recognition
      text = r.recognize_sphinx(audio_text)
      print('Converting audio transcripts into text ...')
      print(text)
