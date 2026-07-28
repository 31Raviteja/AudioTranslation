import time

from config import INPUT_FOLDER
from exceptions.custom_exceptions import AudioPipelineException
from services.audio_converter import AudioConverter
from services.audio_validator import AudioValidator
from services.speech_to_text import SpeechToText
from services.translator import Translator
from utils.file_handler import FileHandler
from utils.logger import logger


class AudioTranslationPipeline:

    def run(self):

        start_time = time.time()

        audio_file = INPUT_FOLDER / "sample.mp3"
        

        logger.info("=" * 60)
        logger.info("Pipeline Started")

        try:

            logger.info("Validating audio file...")
            AudioValidator.validate(audio_file)

            logger.info("Converting audio...")
            wav_file = AudioConverter.convert(audio_file)

            logger.info("Performing Speech-to-Text...")
            text = SpeechToText.transcribe(wav_file)

            logger.info("Translating text...")
            translated = Translator.translate(text)

            logger.info("Saving transcription...")
            FileHandler.save_text(
                "transcription.txt",
                text
            )

            logger.info("Saving translation...")
            FileHandler.save_text(
                "translation.txt",
                translated
            )

            execution_time = round(time.time() - start_time, 2)

            logger.info(
                f"Pipeline Completed Successfully in {execution_time} seconds."
            )

            return {
                "status": "SUCCESS",
                "wav_file": wav_file,
                "text": text,
                "translation": translated,
                "execution_time": execution_time
            }

        except AudioPipelineException as error:

            logger.error(f"Pipeline Failed : {error}")

            print("\n" + "=" * 60)
            print("❌ PIPELINE FAILED")
            print("=" * 60)
            print(error)
            print("=" * 60)

            return None

        except Exception as error:

            logger.exception("Unexpected Error")

            print("\n" + "=" * 60)
            print("❌ UNEXPECTED ERROR")
            print("=" * 60)
            print(error)
            print("=" * 60)

            return None

        finally:

            logger.info("Pipeline Finished")
            logger.info("=" * 60)