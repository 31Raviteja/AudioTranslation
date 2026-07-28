from pathlib import Path

# Project Paths
BASE_DIR = Path(__file__).resolve().parent

INPUT_FOLDER = BASE_DIR / "input_audio"
OUTPUT_FOLDER = BASE_DIR / "output"
LOG_FOLDER = BASE_DIR / "logs"

# Whisper Configuration
WHISPER_MODEL = "base"

# Translation
DEFAULT_TARGET_LANGUAGE = "ml"

# Supported Audio Formats
SUPPORTED_AUDIO_FORMATS = [".mp3", ".wav"]

# Logging
LOG_FILE = LOG_FOLDER / "app.log"