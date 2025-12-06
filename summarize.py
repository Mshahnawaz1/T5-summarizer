from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import time

checkpoint = "SlimeRimuru/billsum_model_summarizer"

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""
    
class Summarizer:
    def __init__(self):
        t1 = time.time()
        print(f"Model and tokenizer are loading...")
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
        t2 = time.time()
        print(f"Model and tokenizer loaded successfully in {t2 - t1} seconds.")

        self.max_length = 500
        self.min_length = 100

    def preprocess_text(self, text):
        text = text.strip().replace("  ", ' ')
        sentences = text.replace('\n', ' ').replace("  ", ' ').replace('\r', ' ')
        
        return "\n".join(sentences)
    
    def chunking_text(self, text, chunk_size=350):
        words = text.split()
        chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
        return chunks

    def pipeline(self, text):
        chunks = self.chunking_text(self.preprocess_text(text))
        if len(chunks) > self.max_length:
            summaries = [self.summarize(chunk) for chunk in chunks]
            result = " ".join(summaries)
        else:
            result = self.summarize(text)
        return result


    def summarize(self, text, max_length=500, min_length=100):
        input_text = "summarize: " + text
        inputs = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

        # Generate summary
        summary_ids = self.model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        return summary
    

if __name__ == "__main__":
    summarizer = Summarizer()
    while True:
        input_text = input("Enter text to summarize (or 'exit' to quit): ")
        if input_text.lower() == 'exit':
            break
        print("Summary:", summarizer.pipeline(input_text))