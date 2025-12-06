# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import time

itime = time.time()
tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google-t5/t5-small")

ftime = time.time()
print(f"Model and tokenizer loaded successfully in {ftime - itime} seconds.")


def summarizer(input, max_length=500, min_length=100):
    summary = summarize_chunks(chunking_text(preprocess_text(input)))
    return summary


def summarize(text, max_length=500, min_length=100):
    input_text = "summarize: " + text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary
def preprocess_text(text):
    text = text.strip().replace("  ", ' ')
    sentences = text.replace('\n', ' ').replace("  ", ' ').replace('\r', ' ')
    
    # return "".join(sentences)
    return sentences

def chunking_text(text, chunk_size=350):
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def summarize_chunks(chunks):
    summaries = [summarize(chunk) for chunk in chunks]
    return " ".join(summaries)

if __name__ == "__main__":
    from dump.text import text

    print("Final Summary:", summarizer(text))