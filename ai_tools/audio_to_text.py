import speech_recognition as sr
import time

def capture_and_transcribe(language: str) -> None:
    """
    Captures audio from the microphone and transcribes it to text using Google's speech recognition API.
    """
    recognizer = sr.Recognizer()
    try:
        print("Please speak into the microphone...")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio_data = recognizer.listen(source)  # Capture audio
            print("Processing audio...")
            text = recognizer.recognize_google(audio_data, language=language)
            print("\nTranscription:")
            print(text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from the speech recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    language = 'ru-RU'
    while True:
      try:
          start_time = time.time()
          capture_and_transcribe(language)
          print(f"Transcription duration: {time.time() - start_time:.2f} seconds")
      except Exception as e:
          print("Error:", e)
