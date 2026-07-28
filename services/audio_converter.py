from pathlib import Path

from pydub import AudioSegment

from config import OUTPUT_FOLDER
from exceptions.custom_exceptions import AudioConversionError
from utils.logger import logger


class AudioConverter:

    @staticmethod
    def convert(input_file: str):

        try:

            OUTPUT_FOLDER.mkdir(exist_ok=True)

            input_path = Path(input_file)

            output_file = OUTPUT_FOLDER / f"{input_path.stem}.wav"

            logger.info("Audio conversion started.")

            audio = AudioSegment.from_file(input_file)

            audio.export(output_file, format="wav")

            logger.info("Audio conversion completed.")

            return str(output_file)

        except Exception as error:
            logger.exception("Audio conversion failed.")
            raise AudioConversionError(str(error))