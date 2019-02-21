import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


class GcloudSpeechText:
    def __init__(self):
        # Instantiates a client
        self.client = speech.SpeechClient()

    def get_text(self, file_name):
        # The name of the audio file to transcribe
        # Loads the audio into memory
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='es-ES')

        # Detects speech in the audio file
        response = self.client.recognize(config, audio)

        for result in response.results:
            return str(result.alternatives[0].transcript)
        return ""
