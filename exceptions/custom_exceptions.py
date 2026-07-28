class AudioPipelineException(Exception):
    """Base exception for the Audio Translation Pipeline."""


class InvalidAudioFile(AudioPipelineException):
    """Raised when the audio file is invalid."""


class AudioConversionError(AudioPipelineException):
    """Raised when audio conversion fails."""


class SpeechRecognitionError(AudioPipelineException):
    """Raised when Whisper transcription fails."""


class TranslationError(AudioPipelineException):
    """Raised when translation fails."""