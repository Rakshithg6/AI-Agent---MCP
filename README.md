# 🧠 AI Customer Support Agent (RAG with Ollama + LangChain + FastAPI + Streamlit)

This project is an AI-powered customer support assistant built using:

- 🤖 LangChain (RAG with FAISS & Ollama)
- 📄 PDF Knowledge Ingestion
- 🔥 FastAPI for backend API
- 🌐 Streamlit for web frontend

## 🚀 Features

- Upload PDF documents to build a custom knowledge base.
- Ask natural language questions about the uploaded content.
- Chat interface powered by Retrieval-Augmented Generation (RAG).
- Powered by local Ollama LLM (e.g. LLaMA2).
- Uses FAISS for vector store & semantic retrieval.

## 🏗️ Project Structure

```bash
ai-customer-support-mcp/
│
├── backend/
│   ├── main.py                # FastAPI server
│   ├── rag_pipeline.py        # Ingest PDF + create vectorstore + build RAG chain
│   ├── agent.py               # Core chat agent logic
│   ├── context_memory.py      # (Optional) Session memory (future use)
│   └── uploads/               # Uploaded PDFs (auto-created)
│
├── app.py                     # Streamlit frontend interface
├── requirements.txt
└── README.md
```

![image](https://github.com/user-attachments/assets/17e6bb96-caad-45f9-9e36-2268ee14a339)
