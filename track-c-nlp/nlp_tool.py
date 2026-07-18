"""
Track C - Nepali-English NLP Tool
-----------------------------------
This starter covers all three NLP tasks for Nepali / code-switched text:
  1. Sentiment analysis (Nepali is natively supported by Azure AI Language)
  2. Translation (Nepali -> English via Azure Translator)
  3. A combined pipeline: translate first, then analyze in English (more accurate)

Prerequisites:
  - Azure AI Language resource (for sentiment analysis)
  - Azure Translator resource (for translation)
  - Both keys and endpoints in your .env file
"""

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.ai.translation.text import TextTranslationClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()


# ─── Client setup ─────────────────────────────────────────────────────────────

def get_language_client() -> TextAnalyticsClient:
    """Initialize the Azure AI Language client."""
    endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
    key = os.environ["AZURE_LANGUAGE_KEY"]
    return TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )


def get_translation_client() -> TextTranslationClient:
    """Initialize the Azure Translator client."""
    key = os.environ["AZURE_TRANSLATOR_KEY"]
    endpoint = os.environ.get(
        "AZURE_TRANSLATOR_ENDPOINT", "https://api.cognitive.microsofttranslator.com"
    )
    region = os.environ["AZURE_TRANSLATOR_REGION"]
    return TextTranslationClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
        region=region,
    )


# ─── Task 1: Sentiment Analysis ──────────────────────────────────────────────

def analyze_sentiment(texts: list[str], language: str = "ne") -> None:
    """
    Run sentiment analysis on Nepali text directly.
    language='ne' is natively supported by Azure AI Language.
    """
    client = get_language_client()
    results = client.analyze_sentiment(texts, language=language)

    print("\n=== Sentiment Analysis Results ===")
    for i, result in enumerate(results):
        if result.is_error:
            print(f"[{i}] Error: {result.error.message}")
            continue

        print(f"\nText:      {texts[i]}")
        print(f"Sentiment: {result.sentiment.upper()}")
        print(
            f"Scores:    Positive={result.confidence_scores.positive:.2f}  "
            f"Neutral={result.confidence_scores.neutral:.2f}  "
            f"Negative={result.confidence_scores.negative:.2f}"
        )

        # Sentence-level breakdown
        for j, sentence in enumerate(result.sentences):
            print(
                f"  Sentence {j+1}: '{sentence.text}' -> {sentence.sentiment} "
                f"(pos={sentence.confidence_scores.positive:.2f})"
            )


# ─── Task 2: Translation ──────────────────────────────────────────────────────

def translate_to_english(texts: list[str]) -> list[str]:
    """
    Translate Nepali text to English using Azure Translator.
    Returns a list of translated strings.
    """
    client = get_translation_client()
    response = client.translate(
        body=texts,
        to_language=["en"],
        from_language="ne",
    )

    translated = []
    print("\n=== Translation Results ===")
    for i, item in enumerate(response):
        eng = item.translations[0].text
        translated.append(eng)
        print(f"Original:   {texts[i]}")
        print(f"Translated: {eng}\n")

    return translated


# ─── Task 3: Combined pipeline ───────────────────────────────────────────────

def translate_then_analyze(texts: list[str]) -> None:
    """
    Translate Nepali to English first, then run sentiment on the English text.
    This tends to be more accurate than running Nepali sentiment directly.
    """
    translated = translate_to_english(texts)
    print("\nRunning sentiment on translated text...")
    analyze_sentiment(translated, language="en")


# ─── Sample test set ──────────────────────────────────────────────────────────

SAMPLE_TEXTS = [
    "मलाई यो सेवा धेरै मन पर्यो।",       # I really liked this service.
    "यो खाना एकदमै नराम्रो थियो।",         # This food was very bad.
    "आज मौसम ठीकठाक छ।",                  # The weather is okay today.
    "यो फिल्म अद्भुत थियो, मलाई धेरै मन पर्यो।",  # This film was wonderful.
    "सेवा ढिलो थियो र कर्मचारी असभ्य थिए।",        # Service was slow and staff were rude.
]

# Manually labeled ground truth for evaluation
LABELS = ["positive", "negative", "neutral", "positive", "negative"]


def evaluate_against_labels(predictions: list[str], labels: list[str]) -> None:
    """Compare model predictions against your manual labels and print accuracy."""
    correct = sum(p == l for p, l in zip(predictions, labels))
    print(f"\n=== Evaluation ===")
    print(f"Accuracy: {correct}/{len(labels)} ({100 * correct / len(labels):.0f}%)")
    for i, (pred, label) in enumerate(zip(predictions, labels)):
        match = "CORRECT" if pred == label else "WRONG"
        print(f"  [{match}] Text {i+1}: predicted={pred}, expected={label}")


def run_evaluation():
    """Run sentiment on sample texts and evaluate against manual labels."""
    client = get_language_client()
    results = client.analyze_sentiment(SAMPLE_TEXTS, language="ne")

    predictions = []
    for result in results:
        if result.is_error:
            predictions.append("error")
        else:
            predictions.append(result.sentiment)

    evaluate_against_labels(predictions, LABELS)


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("Nepali-English NLP Tool")
    print("========================\n")
    print("Choose a task:")
    print("  1 - Sentiment analysis (Nepali direct)")
    print("  2 - Translation (Nepali -> English)")
    print("  3 - Translate then analyze (recommended)")
    print("  4 - Evaluate against sample labeled test set")
    print()

    choice = input("Enter 1, 2, 3, or 4: ").strip()

    if choice == "1":
        analyze_sentiment(SAMPLE_TEXTS)
    elif choice == "2":
        translate_to_english(SAMPLE_TEXTS)
    elif choice == "3":
        translate_then_analyze(SAMPLE_TEXTS)
    elif choice == "4":
        run_evaluation()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
