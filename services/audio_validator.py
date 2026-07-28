from pathlib import Path

from config import SUPPORTED_AUDIO_FORMATS
from exceptions.custom_exceptions import InvalidAudioFile


class AudioValidator:

    @staticmethod
    def validate(audio_path: str):

        path = Path(audio_path)

        if not path.exists():
            raise InvalidAudioFile(
                f"Audio file '{path.name}' does not exist."
            )

        if path.suffix.lower() not in SUPPORTED_AUDIO_FORMATS:
            raise InvalidAudioFile(
                f"Unsupported audio format: {path.suffix}"
            )

        if path.stat().st_size == 0:
            raise InvalidAudioFile(
                "Audio file is empty."
            )

        return True