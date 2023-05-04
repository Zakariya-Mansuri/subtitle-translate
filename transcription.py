import os
import tempfile
import speech_recognition as sr

def transcribe(file_path):

    print("transcribing file:", file_path)
    assert os.path.exists(file_path), f"File {file_path} does not exist"

    r = sr.Recognizer()
    print("file_path:",file_path)
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)
    try:
        transcription = r.recognize_google(audio)
        
    except sr.UnknownValueError:
        transcription = "Speech recognition could not understand audio."
    except sr.RequestError as e:
        transcription = f"Could not request results from speech recognition service; {e}"
    return transcription
        
