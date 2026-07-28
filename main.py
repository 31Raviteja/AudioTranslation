from services.pipeline import AudioTranslationPipeline


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


if __name__ == "__main__":
    main()