from services.pipeline import AudioTranslationPipeline

from database.database import SessionLocal
from database.models import Translation


def main():

    print("=" * 60)
    print("      AUDIO TRANSLATION PIPELINE")
    print("=" * 60)

    pipeline = AudioTranslationPipeline()

    result = pipeline.run()

    if result:

        print("\n✅ Pipeline Completed Successfully")

        print(f"\nWAV File      : {result['wav_file']}")
        print(f"\nOriginal Text : {result['text']}")
        print(f"\nTranslation   : {result['translation']}")

        # Save to MySQL
        db = SessionLocal()

        translation = Translation(
            file_name=result["wav_file"],
            original_text=result["text"],
            language="Unknown",  # Replace if your pipeline returns language
            translated_text=result["translation"]
        )

        db.add(translation)
        db.commit()
        db.close()

        print("\n✅ Saved to MySQL successfully!")


if __name__ == "__main__":
    main()