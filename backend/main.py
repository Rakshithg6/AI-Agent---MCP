from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from .agent import chat_with_agent
from .rag_pipeline import ingest_pdf

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    try:
        uploads_dir = "uploads"
        os.makedirs(uploads_dir, exist_ok=True)

        file_path = os.path.join(uploads_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("[INFO] File saved. Ingesting...")
        ingest_pdf(file_path)
        return {"status": "success", "message": "File uploaded and ingested."}

    except Exception as e:
        print(f"[ERROR] Exception during upload: {e}")
        return {"status": "error", "message": str(e)}

@app.post("/chat")
async def chat(message: str = Form(...), session_id: str = Form("default")):
    try:
        response = chat_with_agent(message, session_id)
        if isinstance(response, dict):
            return {"reply": response.get("answer", "⚠️ No response.")}
        else:
            return {"reply": response}
    except Exception as e:
        print(f"[ERROR] Exception during chat: {e}")
        return {"reply": f"⚠️ Error during chat: {e}"}
