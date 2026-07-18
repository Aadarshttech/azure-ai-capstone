# Track C - Nepali-English NLP Tool

## What this does

Runs three NLP tasks on Nepali and code-switched text using Azure AI Language and Azure Translator:
1. Sentiment analysis directly in Nepali (natively supported)
2. Translation from Nepali to English
3. A combined pipeline: translate first, then run English sentiment (generally more accurate)
4. Evaluation against a manually labeled test set

## Folder structure

```
track-c-nlp/
  nlp_tool.py      <- main script
  README.md
```

## Setup

You need two Azure resources: Azure AI Language and Azure Translator. These are separate services.

### Create Azure AI Language resource
1. Go to https://portal.azure.com
2. Create a resource -> search "Language"
3. Select "Language service" -> Create
4. Copy the **Endpoint** and **Key 1**

### Create Azure Translator resource
1. Go to https://portal.azure.com
2. Create a resource -> search "Translator"
3. Select "Translator" -> Create
4. Copy the **Key**, **Endpoint**, and **Region**

### Fill in your .env

```
AZURE_LANGUAGE_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
AZURE_LANGUAGE_KEY=your_language_key

AZURE_TRANSLATOR_KEY=your_translator_key
AZURE_TRANSLATOR_REGION=eastus
# AZURE_TRANSLATOR_ENDPOINT is optional, defaults to global endpoint
```

### Run

```bash
python nlp_tool.py
```

Then choose task 1, 2, 3, or 4 from the menu.

## Language support note

Azure AI Language supports Nepali (`ne`) natively for sentiment analysis as of 2024. However, the model is less confident on Nepali than on English, which is why the translate-then-analyze pipeline (task 3) often performs better. Test both and compare.

## Extending the test set

Edit the `SAMPLE_TEXTS` and `LABELS` lists at the bottom of `nlp_tool.py` to add your own examples. The evaluation function will automatically compare the model's predictions against your labels and print accuracy.

## Resources

- [Supported languages - Azure AI Language](https://learn.microsoft.com/en-us/azure/ai-services/language-service/concepts/language-support)
- [Sentiment analysis quickstart (Python)](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/quickstart)
- [Azure Translator - Python SDK](https://learn.microsoft.com/en-us/azure/ai-services/translator/quickstart-text-sdk?pivots=programming-language-python)
- [azure-ai-textanalytics PyPI](https://pypi.org/project/azure-ai-textanalytics/)
- [azure-ai-translation-text PyPI](https://pypi.org/project/azure-ai-translation-text/)
- [Explore Azure AI Language (Microsoft Learn path)](https://learn.microsoft.com/en-us/training/paths/explore-natural-language-processing/)
