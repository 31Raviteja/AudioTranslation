import whisper

from config import WHISPER_MODEL
from exceptions.custom_exceptions import SpeechRecognitionError
from utils.logger import logger


class SpeechToText:

    @staticmethod
    def transcribe(audio_file: str):

        try:

            logger.info("Loading Whisper model.")

            model = whisper.load_model(WHISPER_MODEL)

            logger.info("Speech transcription started.")

            result = model.transcribe(audio_file)

            logger.info("Speech transcription completed.")

            return result["text"]

        except Exception as error:
            logger.exception("Speech recognition failed.")
            raise SpeechRecognitionError(str(error))