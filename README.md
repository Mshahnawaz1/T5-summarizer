# 📝 Text Summarizer

An NLP-powered text summarization web app built using T5-small and PyTorch, designed to generate concise summaries from long text inputs.

load the model
```
checkpoint = "SlimeRimuru/billsum_model_summarizer"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

```

## ⚙️ Features

Uses T5-small from Hugging Face for high-quality text summarization

Flask backend for both web and REST API access

Gunicorn deployment for production-ready performance

## 🚀 Tech Stack

Python, Flask, PyTorch, Hugging Face Transformers, HTML/CSS, Gunicorn

## 📦 Installation
``` BASH
git clone https://github.com/Mshahnawaz1/T5-summarizer
cd text-summarizer
pip install -r requirements.txt
python app.py
```


## 💡 Usage

Open the web app and paste your text

Click Summarize to generate concise summaries

Or send a POST request to /summarize endpoint with JSON input

``` bash
curl -X POST http://127.0.0.1:5000/summarize -H "Content-Type: application/json" -d '{"text": "Your text here"}
```


Fine-tuned T5-small model from Hugging Face Transformers
.
