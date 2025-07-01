from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.chat_models import ChatOllama
import os
import shutil

def ingest_pdf(path: str):
    print(f"[INFO] Loading PDF: {path}")
    loader = PyPDFLoader(path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = splitter.split_documents(pages)
    print(f"[INFO] Split into {len(texts)} chunks")

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.from_documents(texts, embeddings)

    # Remove old vectorstore if it exists
    if os.path.exists("vectorstore"):
        try:
            shutil.rmtree("vectorstore")
            print("[INFO] Old vectorstore directory removed.")
        except Exception as e:
            print(f"[ERROR] Failed to remove old vectorstore: {e}")
            raise

    vectorstore.save_local("vectorstore")
    print("[INFO] Vectorstore saved to ./vectorstore")


def get_rag_chain():
    if not os.path.exists("vectorstore"):
        print("⚠️ Vector store not initialized. Please upload a document first.")
        return None

    try:
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        vectorstore = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)

        # Limit retrieval to top 3 results
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        llm = ChatOllama(model="llama2")
        chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True
        )
        print("[INFO] RAG chain initialized successfully.")
        return chain

    except Exception as e:
        print(f"[ERROR] Failed to load vectorstore: {e}")
        return None
