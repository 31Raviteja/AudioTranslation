from deep_translator import GoogleTranslator

from config import DEFAULT_TARGET_LANGUAGE
from exceptions.custom_exceptions import TranslationError
from utils.logger import logger


class Translator:

    @staticmethod
    def translate(text: str):

        try:

            logger.info("Translation started.")

            translated = GoogleTranslator(
                source="auto",
                target=DEFAULT_TARGET_LANGUAGE
            ).translate(text)

            logger.info("Translation completed.")

            return translated

        except Exception as error:
            logger.exception("Translation failed.")
            raise TranslationError(str(error))