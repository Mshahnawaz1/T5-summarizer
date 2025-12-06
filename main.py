from fastapi import FastAPI
from dump.summarize import summarizer

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/summarize/")
async def summarize_text(input_text: str):
    if not input_text.strip():
        return {"summary": "Input text is empty."}
    
    summary = summarizer(input_text)
    return {"summary": summary}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)